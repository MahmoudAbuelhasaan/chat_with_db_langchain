from flask import render_template,request
from flask_login import login_required,current_user
from app.chat import bp
from app import socketio, db
from app.chat.ai import intialize_sql_agent


@bp.route('/chat',methods=['GET', 'POST'])
@login_required
def chat(): 
    return render_template('chat/chat.html')

@socketio.on('message')
@login_required
def handle_message(data):
    user_message = data['message']
    agent = intialize_sql_agent()
    response = agent.invoke({'input':user_message})
    # print(f"User: {user_message}")
    # print(f"Agent: {response}")
    socketio.emit('response', {'response': response['output']})

    
