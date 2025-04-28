"""
主入口文件，提供命令行接口以使用工作流系统
"""
import argparse
from src.core.workflow_manager import WorkflowManager

def main():
    """主函数，处理命令行参数并运行工作流"""
    parser = argparse.ArgumentParser(description="自定义工作流Agent系统")
    parser.add_argument("--input", "-i", type=str, help="用户输入的请求")
    parser.add_argument("--interactive", "-int", action="store_true", help="启用交互模式")
    
    args = parser.parse_args()
    workflow = WorkflowManager()
    
    if args.interactive:
        # 交互模式
        print("=== 工作流Agent系统交互模式 ===")
        print("输入'退出'或'exit'结束交互")
        
        while True:
            user_input = input("\n请输入您的请求: ")
            if user_input.lower() in ['退出', 'exit', 'quit']:
                break
                
            # 处理用户输入
            result = workflow.process(user_input)
            
            # 显示结果摘要
            print("\n=== 处理结果摘要 ===")
            print(f"意图类型: {result['intent'].get('type', 'unknown')}")
            print(f"生成的代码长度: {len(result['code'])} 字符")
            print(f"生成的文档长度: {len(result['documentation'])} 字符")
            
        print("感谢使用工作流Agent系统!")
    
    elif args.input:
        # 使用命令行参数作为输入
        result = workflow.process(args.input)
        
        # 显示结果
        print("\n=== 意图分析结果 ===")
        print(result["intent"])
        
        print("\n=== 生成的代码 ===")
        print(result["code"])
        
        print("\n=== 生成的文档 ===")
        print(result["documentation"])
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()