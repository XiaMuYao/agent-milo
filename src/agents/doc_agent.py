"""
文档生成Agent模块，负责生成代码文档
"""
from src.utils.ai_service import askGPT

class DocAgent:
    """
    文档生成Agent，负责基于代码和意图生成文档
    """
    def __init__(self):
        self.name = "DocAgent"
    
    def generate(self, intent_data, code):
        """
        根据意图和代码生成文档
        
        参数:
            intent_data (dict): 意图数据，包含类型和详情
            code (str): 生成的代码
            
        返回:
            str: 生成的文档
        """
        # 提取意图类型和详情
        intent_type = intent_data.get("type", "unknown")
        details = intent_data.get("details", "")
        
        # 调用askGPT生成文档
        prompt = f"为以下代码生成文档:\n意图类型: {intent_type}\n详情: {details}\n代码:\n{code}"
        documentation = askGPT(prompt)
        
        # 如果没有获得AI回复，使用简单的默认文档模板
        if not documentation:
            return f"""
# 文档

## 概述
这是针对以下意图生成的代码文档："{details}"

## 代码说明
```python
{code}
```

## 使用方法
请参考代码注释了解如何使用此代码。
"""
        
        return documentation 