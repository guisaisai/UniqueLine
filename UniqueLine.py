import sublime
import sublime_plugin

class UniqueLine(sublime_plugin.TextCommand):
    def run(self, edit):
        # 获取当前视图的所有文本
        full_text = self.view.substr(sublime.Region(0, self.view.size()))
        
        # 将文本按行分割，并去除每行前后的空白字符
        lines = full_text.splitlines()
        
        # 过滤空行并去除每行的前后空白
        lines = [line.strip() for line in lines if line.strip()]
        
        # 使用集合去重，保持顺序
        seen = set()
        unique_lines = []
        for line in lines:
            if line not in seen:
                unique_lines.append(line)
                seen.add(line)
        
        # 将去重后的内容重新设置回文本
        self.view.replace(edit, sublime.Region(0, self.view.size()), "\n".join(unique_lines))
