import os
import shutil

# 定义项目的根目录
base_path = "AI-Frontend-Gallery"

# 定义要生成的AI工具和页面
pages = {
    "gpt-4": ["landing-page-v1", "dashboard-ui-v2"],
    "midjourney": ["portfolio-concept-v1"],
    "claude-3": ["ecommerce-v1"],
    "doubao": ["Cyberpunk style with breathing effects"],
    "ChatGPT": ["chat-interface-v1", "prompt-templates-v2"],
        "Gemini": ["multi-modal-demo-v1", "api-docs-v2"],
        "SiliconFlow": ["model-train-dash-v1", "inference-test-v2"],
        "DeepSeek": ["knowledge-base-v1", "task-automate-v2"],
        "万知": ["info-query-v1", "scenario-adapt-v2"],
        "智谱清言": ["text-analyze-v1", "dialog-flow-v2"],
        "Kimi": ["long-text-handle-v1", "qa-optimize-v2"],
        "百小应": ["biz-scene-v1", "user-interact-v2"],
        "通义千问": ["general-qa-v1", "creative-write-v2"],
        "跃问": ["quick-resp-v1", "topic-expand-v2"],
        "豆包": ["Cyberpunk style with breathing effects", "daily-chat-v2"],
        "Cici": ["life-assist-v1", "story-create-v2"],
        "海螺": ["info-agg-v1", "chat-robot-v2"],
        "Groq": ["high-speed-infer-v1", "model-tune-v2"],
        "Claude": ["complex-reason-v1", "content-gen-v2"],
        "文心一言": ["multi-lang-v1", "scene-app-v2"],
        "百度AI搜索": ["search-optim-v1", "result-sort-v2"],
        "腾讯元宝": ["game-ai-v1", "chat-assist-v2"],
        "商量": ["plan-make-v1", "scheme-eval-v2"],
        "SparkDesk": ["work-flow-v1", "collab-tool-v2"],
        "秘塔AI搜索": ["legal-search-v1", "doc-analyze-v2"],
        "Poe": ["multi-model-v1", "chat-manage-v2"],
        "Perplexity": ["knowledge-explore-v1", "answer-refine-v2"],
        "DEV_": ["dev-test-v1", "feature-exp-v2"],
        "天工AI": ["tech-research-v1", "project-help-v2"],
        "HuggingChat": ["open-source-v1", "model-finetune-v2"],
        "Felo": ["lightweight-v1", "quick-chat-v2"],
        "DuckDuckGo": ["privacy-search-v1", "result-filter-v2"],
        "bolt": ["fast-resp-v1", "task-exec-v2"],
        "纳米AI": ["nano-app-v1", "small-task-v2"],
        "纳米AI搜索": ["nano-search-v1", "precise-find-v2"],
        "ThinkAny": ["think-tank-v1", "idea-gen-v2"],
        "Hika": ["life-tool-v1", "daily-help-v2"],
        "GitHub Copilot": ["code-assist-v1", "repo-manage-v2"],
        "Genspark": ["gen-ai-v1", "content-create-v2"],
        "Groq": ["high-eff-infer-v1", "model-optim-v2"],  # 和前面Groq重复，实际可根据情况区分，这里先重复结构
        "QwenLM": ["wen-language-v1", "text-process-v2"],
        "Flowith": ["flow-design-v1", "work-automate-v2"],
        "3MinTop": ["quick-start-v1", "short-task-v2"],
        "AI Studio": ["studio-work-v1", "model-build-v2"],
        "小艺": ["smart-assist-v1", "life-service-v2"],
        "NotebookLM": ["note-ai-v1", "study-help-v2"],
        "Coze": ["coze-app-v1", "chat-flow-v2"],
        "Dify": ["dify-tool-v1", "custom-ai-v2"],
        "WPS灵犀": ["doc-ai-v1", "office-help-v2"],
        "LeChat": ["le-chat-v1", "social-chat-v2"],
        "Abacus": ["data-ai-v1", "analyze-help-v2"],
        "Lambda Chat": ["lambda-chat-v1", "ai-dialog-v2"],
        "Monica": ["monica-chat-v1", "daily-assist-v2"],
        "You": ["you-ai-v1", "personal-ai-v2"],
        "知乎直答": ["zhihu-qa-v1", "topic-answer-v2"]
}

def create_page_structure(ai_tool, page_name):
    """为单个页面创建目录和文件"""
    path = os.path.join(base_path, ai_tool, page_name)
    assets_path = os.path.join(path, "assets")

    # 使用 os.makedirs() 来创建所有父级目录
    os.makedirs(assets_path, exist_ok=True)

    print(f"  - Creating: {path}")

    # 创建核心文件
    with open(os.path.join(path, "index.html"), "w",encoding='utf-8') as f:
        f.write("")

    with open(os.path.join(assets_path, "style.css"), "w", encoding='utf-8') as f:
        f.write("/* AI-generated CSS content goes here */")

    # 创建并写入README文件
    readme_content = f"""# {page_name.replace('-', ' ').title()}

* **AI Tool:** {ai_tool.upper()}
* **Version:** {page_name.split('-')[-1]}

---

### The Prompt

>

### Preview

![Page Preview](./preview.png)

---

[Live Demo on GitHub Pages](https://your-username.github.io/AI-Frontend-Gallery/{ai_tool}/{page_name}/)
"""
    with open(os.path.join(path, "README.md"), "w") as f:
        f.write(readme_content)

def generate_main_readme():
    """生成根目录下的总览README文件"""
    print("\nCreating main README.md gallery...")
    readme_content = "# AI Frontend Gallery\n\nThis repository is a collection of frontend interfaces created by various AI models.\n\n"

    for tool, pages_list in pages.items():
        readme_content += f"## {tool.upper()} Designs\n\n"
        for page in pages_list:
            # 这里的链接和图片路径要确保正确
            # 假设preview.png会在你上传后被手动放入每个目录
            readme_content += f"### {page.replace('-', ' ').title()}\n"
            readme_content += f"![{page} preview](./{tool}/{page}/preview.png)\n"
            readme_content += f"[View Details]({tool}/{page}/)\n\n"

    with open(os.path.join(base_path, "README.md"), "w") as f:
        f.write(readme_content)

def main():
    """主函数，负责执行所有任务"""
    if os.path.exists(base_path):
        shutil.rmtree(base_path)
        print(f"Existing directory '{base_path}' removed.")

    os.makedirs(base_path)
    print(f"Base directory '{base_path}' created.")

    for tool, pages_list in pages.items():
        print(f"\nProcessing {tool.upper()}...")
        for page in pages_list:
            create_page_structure(tool, page)

    generate_main_readme()

    print("\nDirectory structure successfully created! You are ready to start.")
    print("Please add your HTML, CSS content, and 'preview.png' files to the respective folders.")

if __name__ == "__main__":
    main()
