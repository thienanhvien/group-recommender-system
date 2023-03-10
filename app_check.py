from contbased.contbased import content_based_product
import streamlit as st
import pandas as pd

product_data = pd.read_csv('Files/Product_data.csv', index_col=0)
product_images = pd.read_csv('Files/Product_image.csv', index_col=0)

@st.cache_data
def load_data():
    df = pd.read_parquet('ALS_top10.parquet')
    return df

# Load the data using the function
df = load_data()


# Set up the Streamlit app
st.title("Product Recommendation System")

sidebar_option = st.sidebar.radio("Table of Contents", ["Business Understanding", "Collaborative Filtering", "Content-based Filtering"])

if sidebar_option == "Business Understanding":
    st.header("Business Understanding")

    # Add some text about recommendation systems
    st.write("Build a Recommendation System to help Tiki recommends and suggests products for users/customers.")
    st.write("<h1 style='font-size: 20px;'>Collaborative Filtering</h1>", unsafe_allow_html=True)
    st.write("Collaborative filtering relies on the preferences of similar users to offer recommendations to a particular user.")
    st.write("Collaborative does not need the features of the items to be given. Every user and item is described by a feature vector or embedding.")
    st.write("It creates embedding for both users and items on its own. It embeds both users and items in the same embedding space.")
    st.write("It considers other users’ reactions while recommending a particular user. It notes which items a particular user likes and also the items that the users with behavior and likings like him/her likes, to recommend items to that user.")
    st.write("It collects user feedbacks on different items and uses them for recommendations.")
    st.image("https://i0.wp.com/analyticsarora.com/wp-content/uploads/2022/03/collaborative-filtering-shown-visually.png?resize=800%2C600&ssl=1")
    st.write("<h1 style='font-size: 20px;'>Content-Based Filtering</h1>", unsafe_allow_html=True)
    st.write("Content-Based recommender system tries to guess the features or behavior of a user given the item’s features, they react positively to.")
    st.write("It makes recommendations by using keywords and attributes assigned to objects in a database and matching them to a user profile.")
    st.write("The user profile is created based on data derived from a user’s actions, such as purchases, ratings (likes and dislikes), downloads, items searched for on a website and/or placed in a cart, and clicks on product links.")
    st.image("https://www.iteratorshq.com/wp-content/uploads/2021/06/content_based_collaborative_filtering.jpg")
    
    
# elif sidebar_option == "Content-based Filtering":
#     st.header("Content-Based Filtering")

#     # Explain the two types of recommendation systems
#     st.write("<strong>Content-Based Filtering</strong> recommends products based on the accumulated knowledge of users. It consists of a resemblance between the items. The proximity and similarity of the product are measured based on the similar content of the item.", unsafe_allow_html=True)

#     product_names = product_data['product_name'].tolist()

#     # Add a search box for product name
#     search_term = st.text_input('Enter a product name to search:', '')

#     # Filter the product names based on the search term
#     if search_term:
#         product_names = [name for name in product_names if search_term.lower() in name.lower()]

#     if len(product_names) == 0:
#         st.write('No products found for the given search term.')
#     else:
#         # Add a dropdown to select a product
#         selected_product = st.selectbox('Select a product', product_names)

#         # Add a search button
#         if st.button('Search'):
#             # Get the recommendations for the selected product
#             recommendations = content_based_product(selected_product)

#             # Display the recommendations
#             st.write(f'Top 10 products similar to {selected_product}:')

#             # Display the selected product image
#             selected_product_row = product_images[product_images['product_name'] == selected_product].iloc[0]
#             image_col, info_col = st.columns(2)
#             with image_col:
#                 st.image(selected_product_row['image'], caption=selected_product_row['product_name'], use_column_width=True)


#             # Display the corresponding price and brand in the right column
#             with info_col:
#                 st.write(f"<b>Price:</b> {selected_product_row['price']}", unsafe_allow_html=True)

#             # Display the first 5 products in the first column and the remaining 5 products in the second column
#             num_rows = 5
#             cols = st.columns(2)
#             with cols[0]:
#                 for i, row in recommendations.head(num_rows).iterrows():
#                     if row['product_name'] == selected_product:
#                         st.write(row['product_name'], ": **chosen product**", unsafe_allow_html=True)
#                     else:
#                         st.write(row['product_name'])
#                     st.image(row['image'], width=None)
#                     st.write(f"<b>Price:</b> {row['price']}", unsafe_allow_html=True)

#             with cols[1]:
#                 for i, row in recommendations.tail(num_rows).iterrows():
#                     if row['product_name'] == selected_product:
#                         st.write(row['product_name'], ": **chosen product**", unsafe_allow_html=True)
#                     else:
#                         st.write(row['product_name'])
#                     st.image(row['image'], width=None)
#                     st.write(f"<b>Price:</b> {row['price']}", unsafe_allow_html=True)
            
#####################           

# elif sidebar_option == "Content-based Filtering":
#     st.header("Content-Based Filtering")

#     # Explain the two types of recommendation systems
#     st.write("<strong>Content-Based Filtering</strong> recommends products based on the accumulated knowledge of users. It consists of a resemblance between the items. The proximity and similarity of the product are measured based on the similar content of the item.", unsafe_allow_html=True)

#     product_names = product_data['product_name'].tolist()

#     # Add a search box for product name
#     search_term = st.text_input('Enter a product name to search:', '')

#     # Filter the product names based on the search term
#     if search_term:
#         product_names = [name for name in product_names if search_term.lower() in name.lower()]

#     if len(product_names) == 0:
#         st.write('No products found for the given search term.')
#     else:
#         # Add a dropdown to select a product
#         selected_product = st.selectbox('Select a product', product_names)

#         # Add a search button
#         if st.button('Search'):
#             # Get the recommendations for the selected product
#             recommendations = content_based_product(selected_product)

#             # Display the recommendations
#             st.write(f'Top 10 products similar to {selected_product}:')

#             # Display the selected product image
#             selected_product_row = product_images[product_images['product_name'] == selected_product].iloc[0]
#             image_col, info_col = st.columns(2)
#             with image_col:
#                 st.image(selected_product_row['image'], caption=selected_product_row['product_name'], use_column_width=True)


#             # Display the corresponding price and brand in the right column
#             with info_col:
#                 st.write(f"<b>Price:</b> {selected_product_row['price']}", unsafe_allow_html=True)

#             # Display the first 5 products in the first column and the remaining 5 products in the second column
#             num_rows = 5
#             cols = st.columns(2)
#             dropdown_options = []
#             with cols[0]:
#                 for i, row in recommendations.head(num_rows).iterrows():
#                     if row['product_name'] == selected_product:
#                         st.write(row['product_name'], ": **chosen product**", unsafe_allow_html=True)
#                     else:
#                         st.write(row['product_name'])
#                         dropdown_options.append(row['product_name'])
#                     st.image(row['image'], width=None)
#                     st.write(f"<b>Price:</b> {row['price']}", unsafe_allow_html=True)

#             with cols[1]:
#                 for i, row in recommendations.tail(num_rows).iterrows():
#                     if row['product_name'] == selected_product:
#                         st.write(row['product_name'], ": **chosen product**", unsafe_allow_html=True)
#                     else:
#                         st.write(row['product_name'])
#                         dropdown_options.append(row['product_name'])
#                     st.image(row['image'], width=None)
#                     st.write(f"<b>Price:</b> {row['price']}", unsafe_allow_html=True)
            
#             # Add a dropdown to select a recommended product
#             if len(recommendations) > 0:
#                 dropdown_options = recommendations['product_name'].tolist()
#                 selected_recommendation = st.selectbox('Select a recommended product', dropdown_options)

#                 # Get the recommendations for the selected product
#                 recommendations = content_based_product(selected_recommendation)

#                 # Display the recommendations
#                 st.write(f'Next 4 products similar to {selected_recommendation}:')

#                 # Display the selected product image
#                 selected_product_row = product_images[product_images['product_name'] == selected_recommendation].iloc[0]
#                 image_col, info_col = st.columns(2)
#                 with image_col:
#                     st.image(selected_product_row['image'], caption=selected_product_row['product_name'], use_column_width=True)

#                 # Display the corresponding price and brand in the right column
#                 with info_col:
#                     st.write(f"<b>Price:</b> {selected_product_row['price']}", unsafe_allow_html=True)

#                 # Display the recommended products
#                 cols = st.columns(4)
#                 for i, row in recommendations.head(4).iterrows():
#                     with cols[i % 4]:
#                         st.image(row['image'], width=None)
#                         st.write(row['product_name'])
#                         st.write(f"<b>Price:</b> {row['price']}", unsafe_allow_html=True)

#             else:
#                 st.write("Sorry, no recommendations were found for this product.")

##################

# elif sidebar_option == "Content-based Filtering":
#     st.header("Content-Based Filtering")

#     # Explain the two types of recommendation systems
#     st.write("<strong>Content-Based Filtering</strong> recommends products based on the accumulated knowledge of users. It consists of a resemblance between the items. The proximity and similarity of the product are measured based on the similar content of the item.", unsafe_allow_html=True)

#     product_names = product_data['product_name'].tolist()

#     # Add a search box for product name
#     search_term = st.text_input('Enter a product name to search:', '')

#     # Filter the product names based on the search term
#     if search_term:
#         product_names = [name for name in product_names if search_term.lower() in name.lower()]

#     if len(product_names) == 0:
#         st.write('No products found for the given search term.')
#     else:
#         # Add a dropdown to select a product
#         selected_product = st.selectbox('Select a product', product_names)

#         # Add a search button
#         if st.button('Search'):
#             # Get the recommendations for the selected product
#             recommendations = content_based_product(selected_product)

#             # Display the recommendations
#             st.write(f'Top 10 products similar to {selected_product}:')

#             # Display the recommended products with a button to show more recommendations
#             for i, row in recommendations.iterrows():
#                 with st.expander(f"{row['product_name']}: Show 4 more recommendations"):
#                     # Get the additional recommendations for the selected product
#                     additional_recommendations = content_based_product(row['product_name']).head(4)

#                     # Display the selected product image
#                     selected_product_row = product_images[product_images['product_name'] == row['product_name']].iloc[0]
#                     image_col, info_col = st.columns(2)
#                     with image_col:
#                         st.image(selected_product_row['image'], caption=selected_product_row['product_name'], use_column_width=True)

#                     # Display the corresponding price and brand in the right column
#                     with info_col:
#                         st.write(f"<b>Price:</b> {selected_product_row['price']}", unsafe_allow_html=True)

#                     # Display the recommended products
#                     cols = st.columns(4)
#                     for j, additional_row in additional_recommendations.iterrows():
#                         with cols[j % 4]:
#                             st.image(additional_row['image'], width=None)
#                             st.write(additional_row['product_name'])
#                             st.write(f"<b>Price:</b> {additional_row['price']}", unsafe_allow_html=True)


#####################

elif sidebar_option == "Content-based Filtering":
    st.header("Content-Based Filtering")

    # Explain the two types of recommendation systems
    st.write("<strong>Content-Based Filtering</strong> recommends products based on the accumulated knowledge of users. It consists of a resemblance between the items. The proximity and similarity of the product are measured based on the similar content of the item.", unsafe_allow_html=True)

    product_names = product_data['product_name'].tolist()

    # Add a search box for product name
    search_term = st.text_input('Enter a product name to search:', '')

    # Filter the product names based on the search term
    if search_term:
        product_names = [name for name in product_names if search_term.lower() in name.lower()]

    if len(product_names) == 0:
        st.write('No products found for the given search term.')
    else:
        # Add a dropdown to select a product
        selected_product = st.selectbox('Select a product', product_names)

        # Add a search button
        if st.button('Search'):
            # Get the recommendations for the selected product
            recommendations = content_based_product(selected_product)

            # Display the recommendations
            st.write(f'Recommended products similar to {selected_product}:')

            # Display the top 10 recommended products and their images
            top_10_products = recommendations.head(10)
            cols = st.columns(5)
            product_name_height = 300 # set a fixed height for the product names
            for i, row in top_10_products.iterrows():
                with cols[i % 5]:
                    # Set a fixed height for the images
                    st.image(row['image'])
                    # Set a fixed height for the product names
                    st.write(f'<div style="height:{product_name_height}px;overflow-y:auto">{row["product_name"]}</div>', unsafe_allow_html=True)

            st.write('<strong>For more recommendations:<strong>', unsafe_allow_html=True)

            # Display the recommended products with a button to show more recommendations
            for i, row in recommendations.iterrows():
                with st.expander(f"{row['product_name']}: Show 4 more recommendations"):
                    # Get the additional recommendations for the selected product
                    additional_recommendations = content_based_product(row['product_name']).head(4)

                    

                    # Display the selected product image
                    selected_product_row = product_images[product_images['product_name'] == row['product_name']].iloc[0]
                    image_col, info_col = st.columns(2)
                    with image_col:
                        st.image(selected_product_row['image'], caption=selected_product_row['product_name'], use_column_width=True)

                    # Display the corresponding price and brand in the right column
                    with info_col:
                        st.write(f"<b>Price:</b> {selected_product_row['price']}", unsafe_allow_html=True)

                    # Display the recommended products
                    cols = st.columns(4)
                    for j, additional_row in additional_recommendations.iterrows():
                        with cols[j % 4]:
                            st.image(additional_row['image'], width=None)
                            st.write(additional_row['product_name'])
                            st.write(f"<b>Price:</b> {additional_row['price']}", unsafe_allow_html=True)

elif sidebar_option == "Collaborative Filtering":
    st.header("Collaborative Filtering")

    st.write("<strong>Collaborative Filtering</strong> recommends products based on based on the user's historical choices. It focuses on relationships between the item and users; items’ similarity is determined by their rating given by customers who rated both the items.", unsafe_allow_html=True)

    st.write('Select your customer ID from the dropdown list to get personalized product recommendations')

    # Get the customer IDs from the data
    customer_ids = df['customer_id'].unique()

    # Create a search bar for the customer ID
    selected_customer_id = st.text_input('Enter a customer ID to search:')

    # Or create a dropdown menu for the customer ID
    if not selected_customer_id:
        selected_customer_id = st.selectbox('Select a customer ID', customer_ids)

    # Create a search button
    search_button = st.button('Search')

    # Check if the search button is clicked
    if search_button:
        # Check if the selected customer ID is valid
        if selected_customer_id in customer_ids:
            # Get the top recommended products for the customer
            num_recommendations = 10
            recommended_products = df[df['customer_id'] == selected_customer_id].sort_values('predict_rating', ascending=False).head(num_recommendations)

            # Display the recommended products
            if not recommended_products.empty:
                st.write('Top Recommended Products:')
                num_rows = 5
                cols = st.columns(2)
                with cols[0]:
                    for i, row in recommended_products.head(num_rows).iterrows():
                        # Display the recommended product
                        st.write(row['item_name'])
                        st.image(row['image'], width=None)
                        st.write(f"<b>Rating:</b> {row['predict_rating']:.2f}", unsafe_allow_html=True)
                        
                with cols[1]:
                    for i, row in recommended_products.tail(num_rows).iterrows():
                        # Display the recommended product
                        st.write(row['item_name'])
                        st.image(row['image'], width=None)
                        st.write(f"<b>Rating:</b> {row['predict_rating']:.2f}", unsafe_allow_html=True)

            else:
                st.write(f"No recommendations found for customer {selected_customer_id}")

        else:
            st.write('Invalid customer ID. Please select a valid customer ID from the dropdown list or enter a valid customer ID in the search bar.')
