from flask import Blueprint

bp = Blueprint('admin', __name__)

from app.admin import routs

bp.add_url_rule('/admin/manage_users', view_func=routs.manage_users, methods=['GET'])
bp.add_url_rule('/admin/update_user_role', view_func=routs.update_user_role, methods=['POST'])
bp.add_url_rule('/admin/dashboard', view_func=routs.dashboard, methods=['GET'])
