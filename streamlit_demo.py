import streamlit as st
import pandas as pd
import numpy as np
if np == "🔨 Test Recommendation":

        st.header("Test the Recommendations")

        st.info("Upon the first opening the data will start loading."
                "\n Unfortunately there is no progress verbose in streamlit. Look in your console.")

        st.success('Data is loaded!')

        models = load_models(device)
        st.success('Models are loaded!')

        state, action, reward, next_state, done = get_batch(device)

        st.subheader('Here is a random batch sampled from testing environment:')
        if st.checkbox('Print batch info'):
            st.subheader('State')
            st.write(state)
            st.subheader('Action')
            st.write(action)
            st.subheader('Reward')
            st.write(reward.squeeze())

        st.subheader('(Optional) Select the state are getting the recommendations for')

        action_id = np.random.randint(0, state.size(0), 1)[0]
        action_id_manual = st.checkbox('Manually set state index')
        if action_id_manual:
            action_id = st.slider("Choose state index:", min_value=0, max_value=state.size(0))

        st.write('state:', state[action_id])
