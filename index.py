import streamlit as st
import traceback
# from ai_engine.agent_media import main as agent_media_main
# from ai_engine.agent_general import main as agent_general_main
from helpers.st_logging import logger
# from helpers.housekeeping import delete_old_files
import streamlit_antd_components as sac
from where2where_app import main as where2where_main
# streamlit run --server.port=8080 --server.baseUrlPath media-baba --browser.gatherUsageStats=false index.py
# DEV --> streamlit run --server.port=8080 --server.baseUrlPath WHERE2WHERE --browser.gatherUsageStats=false index.py


if __name__ == "__main__":

    st.set_page_config(
        layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
        page_title='WHERE2WHERE',  # String or None. Strings get appended with "• Streamlit".
        page_icon=':boomerang:',  # String, anything supported by st.image, or None.
    )

    hide_streamlit_style = """
                 <style>  
                 /* Reduce Top header padding */
                #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}

                /*Reduce Spacing between widgets*/
                div[data-testid="stVerticalBlock"] {
                 gap: 0.5rem;
                 }

                /*Hide Streamlit Menu and various Hides*/
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }

                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }

                /*Make columns only as wide as the buttons (Eg:- for play and reset buttons in SQL)*/
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }

                /*Disable input instructions*/
                div[data-testid="InputInstructions"] > span:nth-child(1) {
                   visibility: hidden; }

                /* Disable fullscreen button on images */ 
                button[title="View fullscreen"]{
                visibility: hidden;}

                /* Display Footer elements*/

                .footer {
                 position: fixed;
                 left: 0;
                 bottom: 0;
                 width: 100%;
                 background-color: white;
                 color: grey;
                 text-align: center;
                 }

                 /* Remove link underline from some buttons like Share */
                 a:link, a:visited {
                    color: inherit;
                    background-color: transparent;
                    text-decoration: none;
                    }

                </style>


    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.header(':boomerang: :grey[WHERE2WHERE]', divider='rainbow', anchor=False, help='Get Geo Distances and more...')
    # st.write("##")
    # ai_mode = sac.switch(label='', value=False, align='start', description='', position='right', size='md',
    #                      on_color='yellow',
    #                      off_color=None, on_label='AI Mode: Text', radius=3,
    #                      off_label='AI Mode: Media')

    try:
        # if ai_mode:
        #     agent_general_main()
        # else:
        #     agent_media_main()

        where2where_main()
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
