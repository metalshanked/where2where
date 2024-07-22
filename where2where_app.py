import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_js_eval import get_geolocation
import streamlit_antd_components as sac
from domain.geo_actions import get_geo_address, get_geo_distance, calculate_travel_fee
import time


def main():

    with st.sidebar:
        with stylable_container(
                key="container_with_border",
                css_styles="""
                                    {
                                        border: 1px solid rgba(49, 51, 63, 0.2);
                                        border-radius: 0.5rem;
                                        padding: calc(1em - 1px)
                                    }
                                    """,
        ):
            auto_location = sac.switch(label='', value=True, align='start', description='', position='right', size='md',
                                       on_color='yellow',
                                       off_color=None, on_label='Auto Location', radius=3,
                                       off_label='Auto Location')
            st.write('**Distance and Cost**')
            data_table = st.data_editor(data={"from_miles":[0,50,75,100,150], "to_miles":[49,74,99,150,99999],
                                              "cost_usd)":[0,50,75,100,150]},
                                        key=None,use_container_width=False,
                                        column_config={
                                            'from_miles': st.column_config.NumberColumn("From", width="small",
                                                                                         help="The From value for the "
                                                                                              "distance range in Miles"),
                                            'to_miles': st.column_config.NumberColumn("To", width="small",
                                                                                         help="The To value for the "
                                                                                              "distance range in Miles"),

                                            'cost_usd': st.column_config.NumberColumn("Cost", width="small",
                                                                                    help="The Cost for the distance "
                                                                                         "range in USD"),


                                        }

                                        )

    with stylable_container(
            key="container_with_border",
            css_styles="""
                            {
                                border: 1px solid rgba(49, 51, 63, 0.2);
                                border-radius: 0.5rem;
                                padding: calc(1em - 1px)
                            }
                            """,
    ):

        with st.container():
            if auto_location:
                dict_location_info = get_geolocation()

                if not dict_location_info:
                    st.toast("Please Enable Location Permissions.", icon="🔥")
                    st.warning("Unable to get location info. Please disable auto location.")
                    return
                location_info = get_geo_address(dict_location_info)
                location_source = st.text_input("Enter source location", disabled=True,value=location_info)
            else:
                location_source = st.text_input("Enter source location")

            location_destination = st.text_input("Enter destination location")

            submit_button = st.button("Submit")


            if location_source and location_destination and submit_button:
                miles = get_geo_distance(location_source, location_destination)
                cost = calculate_travel_fee(miles, data_table)
                st.success(f"The travel fee for {miles:.3f} miles is: ${cost}")


