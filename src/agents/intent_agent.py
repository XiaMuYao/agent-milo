"""
意图分析Agent模块，负责分析用户输入的意图
"""
from src.utils.ai_service import askGPT

class IntentAgent:
    """
    意图分析Agent，负责解析用户输入并确定用户意图
    """
    def __init__(self):
        self.name = "IntentAgent"
    
    def analyze(self, user_input):
        """
        分析用户输入的意图
        
        参数:
            user_input (str): 用户输入的文本
            
        返回:
            dict: 包含意图类型和详细信息的字典
        """
        # 调用askGPT来获取AI的分析结果
        response = askGPT(f"分析以下用户输入的意图:\n{user_input}")
        
        # 如果没有获得AI回复，使用简单的规则进行意图判断
        if not response:
            # 根据关键词简单判断意图类型
            if "如何" in user_input or "怎么" in user_input:
                return {"type": "question", "details": user_input}
            elif "生成" in user_input or "创建" in user_input:
                return {"type": "generation", "details": user_input}
            else:
                return {"type": "unknown", "details": user_input}
        
        return response 