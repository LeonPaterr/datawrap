-- run
streamlit run app.py

Put the config file in ~/.streamlit/config to increase upload limit

App and Multiapp manage the page management to structure the sidemenu and to separate so that it is not all cluttered into a single file
Each Side-bar item is handled in the respected /app/<name.py>, to add to the sidebar, create a new file in /apps/ with the name of the sidebar, import it within app.py and add the app using app.add_app("")

"Helper.py" does some styling and can be used for some generic methods used in every page


