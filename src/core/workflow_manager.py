"""
工作流管理器模块，协调各个Agent的工作
"""
from src.agents.intent_agent import IntentAgent
from src.agents.code_agent import CodeAgent
from src.agents.doc_agent import DocAgent

class WorkflowManager:
    """
    工作流管理器，协调三个Agent的工作流程
    """
    def __init__(self):
        """初始化工作流管理器，创建所需的Agent实例"""
        self.intent_agent = IntentAgent()
        self.code_agent = CodeAgent()
        self.doc_agent = DocAgent()
    
    def process(self, user_input):
        """
        处理用户输入，执行完整的工作流
        
        参数:
            user_input (str): 用户输入的文本
            
        返回:
            dict: 包含意图分析结果、生成的代码和文档的字典
        """
        # 步骤1: 分析意图
        intent_data = self.intent_agent.analyze(user_input)
        print(f"意图分析结果: {intent_data}")
        
        # 步骤2: 生成代码
        code = self.code_agent.generate(intent_data)
        print("生成的代码:")
        print(code)
        
        # 步骤3: 生成文档
        documentation = self.doc_agent.generate(intent_data, code)
        print("生成的文档:")
        print(documentation)
        
        # 返回处理结果
        return {
            "intent": intent_data,
            "code": code,
            "documentation": documentation
        }

