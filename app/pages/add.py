import streamlit as st
from controllers.contact_controller import createContact

class ContactPage :

        st.title("Me contacter ( create )")
        with  st.form(key="contact_form",clear_on_submit=True):
            name  = st.text_input(label= 'Votre nom')
            email = st.text_input(label='Votre email') 
            phone= st.text_input(label='Votre numéro de téléphone')
            message = st.text_area(label='Le message')
            submit_button = st.form_submit_button(label="Envoyer")
            form_data = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "message": message
                }
            if submit_button:            
                if not name or not email or not phone or not message:                  
                    st.error("Tous les champs sont obligatoires.")            
                else:                     
                        response = createContact(name,email,phone,message)                                     
                        if response :
                            st.toast('Merci',icon='😂')
                            st.success('Le message à été envoyé avec succes')
                            # Redirection après succès
                            st.switch_page('pages/read.py')                                                
                        else : 
                            st.error('Votre message n\'a pas puis etre envoyé ')
                   
                    

                
               
      

   