"""
工作流测试模块
"""
import unittest
from src.core.workflow_manager import WorkflowManager
from src.agents.intent_agent import IntentAgent
from src.agents.code_agent import CodeAgent
from src.agents.doc_agent import DocAgent

class TestWorkflow(unittest.TestCase):
    """工作流测试类"""
    
    def setUp(self):
        """测试前准备"""
        self.workflow = WorkflowManager()
    
    def test_intent_agent(self):
        """测试意图分析Agent"""
        agent = IntentAgent()
        result = agent.analyze("生成一个计算斐波那契数列的函数")
        self.assertEqual(result.get("type"), "generation")
    
    def test_code_agent(self):
        """测试代码生成Agent"""
        agent = CodeAgent()
        intent_data = {"type": "generation", "details": "生成一个计算斐波那契数列的函数"}
        code = agent.generate(intent_data)
        self.assertIsNotNone(code)
        self.assertGreater(len(code), 0)
    
    def test_doc_agent(self):
        """测试文档生成Agent"""
        agent = DocAgent()
        intent_data = {"type": "generation", "details": "生成一个计算斐波那契数列的函数"}
        code = "def fibonacci(n):\n    pass"
        doc = agent.generate(intent_data, code)
        self.assertIsNotNone(doc)
        self.assertGreater(len(doc), 0)
    
    def test_workflow_process(self):
        """测试完整工作流程"""
        result = self.workflow.process("生成一个计算斐波那契数列的函数")
        self.assertIn("intent", result)
        self.assertIn("code", result)
        self.assertIn("documentation", result)


if __name__ == "__main__":
    unittest.main() 