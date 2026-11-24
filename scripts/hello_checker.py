def check_case_title(title: str) -> bool:
    """检查用例标题是否非空且长度合理"""
    return bool(title.strip()) and 4 <= len(title) <= 100

if __name__ == "__main__":
    print(check_case_title("登录成功"))