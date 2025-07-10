# 定义项目的根目录。脚本会在这里创建所有的文件夹。
# 你可以根据需要修改此路径。
$basePath = ".\AI-Frontend-Showcase"

# 检查根目录是否存在，如果不存在则创建
if (-not (Test-Path $basePath)) {
    Write-Host "Creating base directory: $basePath"
    New-Item -ItemType Directory -Path $basePath | Out-Null
} else {
    Write-Host "Base directory already exists: $basePath"
}

# 进入根目录，开始创建子文件夹
Set-Location -Path $basePath

Write-Host "`nCreating directory structure..."

# --- 创建 gpt-4 项目文件夹及其内容 ---
$gpt4Path = "gpt-4"
New-Item -ItemType Directory -Path $gpt4Path | Out-Null

$page1Path = "$gpt4Path\landing-page-v1"
New-Item -ItemType Directory -Path $page1Path | Out-Null
New-Item -ItemType File -Path "$page1Path\index.html" | Out-Null
New-Item -ItemType File -Path "$page1Path\preview.png" | Out-Null
New-Item -ItemType File -Path "$page1Path\prompt.txt" | Out-Null
New-Item -ItemType Directory -Path "$page1Path\assets" | Out-Null
New-Item -ItemType File -Path "$page1Path\assets\style.css" | Out-Null
New-Item -ItemType File -Path "$page1Path\assets\script.js" | Out-Null

$page2Path = "$gpt4Path\dashboard-ui-v2"
New-Item -ItemType Directory -Path $page2Path | Out-Null
New-Item -ItemType File -Path "$page2Path\index.html" | Out-Null
New-Item -ItemType File -Path "$page2Path\preview.jpg" | Out-Null
New-Item -ItemType File -Path "$page2Path\prompt.txt" | Out-Null
New-Item -ItemType Directory -Path "$page2Path\assets" | Out-Null
New-Item -ItemType File -Path "$page2Path\assets\style.css" | Out-Null

# --- 创建 midjourney 项目文件夹及其内容 ---
$mjPath = "midjourney"
New-Item -ItemType Directory -Path $mjPath | Out-Null

$page3Path = "$mjPath\portfolio-concept-v1"
New-Item -ItemType Directory -Path $page3Path | Out-Null
New-Item -ItemType File -Path "$page3Path\index.html" | Out-Null
New-Item -ItemType File -Path "$page3Path\preview.png" | Out-Null
New-Item -ItemType File -Path "$page3Path\prompt.txt" | Out-Null
New-Item -ItemType Directory -Path "$page3Path\assets" | Out-Null
New-Item -ItemType File -Path "$page3Path\assets\style.css" | Out-Null
New-Item -ItemType File -Path "$page3Path\assets\script.js" | Out-Null

Write-Host "`nDirectory structure created successfully!"
Write-Host "You can find it at: $basePath"

# 恢复到脚本运行前的目录
Set-Location -Path (Get-Location -Stack)
