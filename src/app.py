import streamlit as st
import stegano
from PIL import Image

st.set_page_config('Stegano Project')

msg = 'Python'

option = st.sidebar.selectbox('Select Menu:', ('Hide Text', 'Reveral Text',
                                               'Hide Photo', 'Unhide photo'))

if option == 'Hide Text':
        host_pic = st.file_uploader('Select file for upload:', ['png', 'jpg'])
        secrect_text = st.text_area('Enter text to hide in your picture:')

        if host_pic and secrect_text:
              if st.button('Hide'):
                    tmp_img = Image.open(host_pic)
                    secret_img = stegano.lsb.hide(tmp_img, secrect_text)
                    secret_img.save('./final_img_save.png')
                    st.success('The text hide in picture.')

if option == 'Reveral Text':
    final_img = st.file_uploader('Select image for reveral:', ['png', 'jpg'])

    if final_img:
          tmp_img = Image.open(final_img)
          reveral_text = stegano.lsb.reveal(tmp_img)

          if st.button('Reveral'):
                if reveral_text != None:
                      st.write(f'Your secrect text: {reveral_text}')
                      st.success('Text reveraled')

                else:
                      st.write('Text not found!')

if option == 'Hide Photo':
      cover_file = st.file_uploader('Select host photo:', type=['png', 'jpg'])
      secret_file = st.file_uploader('Select secrect photo', type=['png', 'jpg'])
      secret_temp =  secret_file.read()
      secrect_text = secret_temp.decode('latin-1')
      if st.button('Hide photo'):
            final_img = stegano.lsb.hide(cover_file, secrect_text)
            final_img.save('./final_img_save.png')
            st.success('Photo hide successfuly...')

if option == 'Unhide photo':
      final_img = st.file_uploader('Select fibal photo:', type=['png', 'jpg'])

      if final_img:
            encode_img = Image.open(final_img)

            if encode_img:
                  if st.button('Reveral photo'):
                        secrect_text = stegano.lsb.reveal(encode_img)
                        temp_img = secrect_text.encode('latin=1')
                        with open('./', 'wb') as f:
                              f.write(temp_img)

                        st.success('Gust picuter recreated...')
                        st.image('./')


#End Program.
