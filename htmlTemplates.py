css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVczOjHNn6qtwF2zV_lBPZ-xsuEgxpFo2Yf88BTaDK8Q&s" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://media.licdn.com/dms/image/D4D03AQFXMaSVCvha8Q/profile-displayphoto-shrink_400_400/0/1691880789430?e=2147483647&v=beta&t=DQCqzKVEPjBWgTFB8as0uZcSQ58pnWOVmFPwxFD_XDI">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
