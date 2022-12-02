from flask import current_app, request
from wxService import wxService_bp

import os
env = os.environ

# https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/ThirdParty/token/component_verify_ticket.html
@wxService_bp.route('/UpdateComponentVerifyTicket', methods=["GET", "POST"])
def update_component_verify_ticket(*args, **kwargs):
    reqArgs, reqForm, reqJson = request.args, request.form, request.get_json(silent=True)
    print(reqForm)
    return "success"