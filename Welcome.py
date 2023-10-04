# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page


LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="pypipo",
        page_icon="👋",
    )

    st.write("# Welcome to pypipo demo page! :smile:")

    # st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        > PyPipo is Python library to convert PIPO Painting canvas image.
        # 🤔 What is Pipo Painting?
        "Pipo Painting" is also called "Paint by Number" or "Painting by Numbers".
        > It is a kit having a board on which light markings to indicate areas to paint, and each area has a number and a corresponding numbered paint to use. The kits come with little compartmentalised boxes where the numbered colour pigments are stored. The users are encouraged to wash the paintbrush every time a new numbered colour is being used.

    """
    )

    if st.button('Let\'s pipo!', type='primary'):
        # go to pipo converter page
        switch_page("Pipo converter")



if __name__ == "__main__":
    run()
