"""
简单使用示例
"""
from src.core.workflow_manager import WorkflowManager

# 创建工作流管理器
workflow = WorkflowManager()

def run_example():
    """运行一个简单的示例"""
    print("=== 工作流Agent系统示例 ===")
    print("请输入您的请求（例如：'生成一个计算斐波那契数列的函数'）：")
    user_input = input("> ")
    
    # 处理用户输入
    result = workflow.process(user_input)
    
    # 打印结果摘要
    print("\n=== 处理结果摘要 ===")
    print(f"意图类型: {result['intent'].get('type', 'unknown')}")
    print(f"生成的代码长度: {len(result['code'])} 字符")
    print(f"生成的文档长度: {len(result['documentation'])} 字符")


if __name__ == "__main__":
    run_example() 