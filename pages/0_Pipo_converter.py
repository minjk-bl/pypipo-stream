import streamlit as st
import pandas as pd
from io import StringIO
from PIL import Image
from pypipo.convert import pipo_convert
from libs.pypipo_custom import PaintingWithData
from pypipo.libs.process import LineDrawing, ColorspaceIndexing
from pypipo.libs.utils import *
from datetime import datetime

uploaded_file = st.file_uploader("Choose an image file to convert", type=['png', 'jpg'])
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.image(bytes_data)

    st.write(uploaded_file.name)

    do_convert = st.button("Convert", type="primary")
    if do_convert:
        # from pypipo.convert import pipo_convert
        # pipo_convert(INPUT_FILE_PATH, OUTPUT_FILE_PATH)

        # ----------------------------
        # Unpack pipo_convert to use PaintingWithData
        # ----------------------------
        # pipo_convert default params
        color_label = True

        # create Painting object using bytes data of image
        status = st.progress(0, text='(1/5) Starting Conversion...')
        painting = PaintingWithData(bytes_data)

        status.progress(20, text='(2/5) Gathering colors...')
        painting_img, color_index_map = painting.run()
        color_indexs, color_rbg_values = painting.get_clustered_color_info(painting_img)

        status.progress(40, text='(3/5) Drawing border lines...')
        drawing = LineDrawing(color_index_map)
        line_drawn_image = drawing.run(outline = True)
        img_lab, lab = drawing.get_image_lab(color_rbg_values, painting_img)

        status.progress(60, text='(4/5) Numbering color spaces...')
        numbering = ColorspaceIndexing(painting_img, line_drawn_image, color_indexs, color_rbg_values)
        output = numbering.run(img_lab, lab, color_label = color_label)

        # Use download component instead of output path
        # img_save(outputpath, output)
        status.progress(80, text='(5/5) Wraping up the progress...')
        binary_cv = cv2.imencode('.PNG', output)[1].tobytes()
        st.image(binary_cv)

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

        status.progress(100, text='Finished!')
        st.success('Successfully converted!', icon="🎉")
        st.balloons()

        # Enable download button
        btn = st.download_button(
            label="Download pipo image",
            data=binary_cv,
            file_name="pypipo_{}.png".format(timestamp),
            mime="image/png"
        )
