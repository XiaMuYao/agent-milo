"""
代码生成Agent模块，负责根据意图生成代码
"""
from src.utils.ai_service import askGPT

class CodeAgent:
    """
    代码生成Agent，负责基于理解的用户意图生成代码
    """
    def __init__(self):
        self.name = "CodeAgent"
    
    def generate(self, intent_data):
        """
        根据意图生成代码
        
        参数:
            intent_data (dict): 意图数据，包含类型和详情
            
        返回:
            str: 生成的代码
        """
        # 提取意图类型和详情
        intent_type = intent_data.get("type", "unknown")
        details = intent_data.get("details", "")
        
        # 调用askGPT来获取生成的代码
        prompt = f"根据以下意图生成代码:\n类型: {intent_type}\n详情: {details}"
        code = askGPT(prompt)
        
        # 如果没有获得AI回复，使用简单的默认代码
        if not code:
            if intent_type == "generation":
                return "# 这里是生成的示例代码\ndef example_function():\n    print('这是由CodeAgent生成的代码')"
            else:
                return "# 无法基于当前意图生成代码"
        
        return code 