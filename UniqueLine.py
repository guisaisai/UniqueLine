import sublime
import sublime_plugin

class UniqueLine(sublime_plugin.TextCommand):
    def run(self, edit):
        # 获取当前视图的所有文本区域
        region = sublime.Region(0, self.view.size())
        
        # 使用集合存储已处理的行
        seen = set()

        # 获取所有行的Region
        lines = self.view.lines(region)
        
        # 记录待删除的区域
        lines_to_delete = []

        # 逐行遍历文本区域
        for line_region in lines:
            line = self.view.substr(line_region).strip()  # 获取每一行并去除前后的空白字符
            
            # 如果是第一次看到该行，则保留它
            if line and line not in seen:
                seen.add(line)
            else:
                # 如果已经见过该行，则记录需要删除的行区域
                lines_to_delete.append(line_region)

        # 删除重复的行
        for line_region in reversed(lines_to_delete):
            self.view.erase(edit, line_region)

