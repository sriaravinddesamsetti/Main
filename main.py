import streamlit as st
from subprocess import call
if st.button('send'):
    call('echo "Body of the email" | mutt -s "Subject" desam@synopsys.com', shell=True)