"""
raos 的运维笔记 - 个人站点
运行在 8.147.64.234 上，从零搭建的云原生项目
"""
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

NOTES = [
    {"title": "Docker 容器化实战", "date": "2026-05", "status": "学习中",
     "desc": "Dockerfile 编写、镜像分层、Docker Compose 多服务编排"},
    {"title": "Linux 系统管理", "date": "2026-04", "status": "已完成",
     "desc": "用户权限、进程管理、systemd、Shell 脚本自动化"},
    {"title": "Nginx 反向代理 & HTTPS", "date": "2026-05", "status": "已完成",
     "desc": "虚拟主机配置、SSL/TLS 证书、Let's Encrypt 自动续期"},
    {"title": "阿里云 ECS 运维", "date": "2026-05", "status": "进行中",
     "desc": "安全组、快照、监控告警、Terraform 基础设施即代码"},
    {"title": "Kubernetes 入门", "date": "2026-06", "status": "待学习",
     "desc": "Pod/Service/Ingress、Deployment 滚动更新、ConfigMap"},
    {"title": "Prometheus + Grafana 监控", "date": "2026-06", "status": "待学习",
     "desc": "指标采集、告警规则、Grafana Dashboard 可视化"},
    {"title": "CI/CD 流水线", "date": "2026-07", "status": "待学习",
     "desc": "GitLab CI、GitHub Actions、自动构建部署"},
    {"title": "TCP/IP 网络原理", "date": "2026-04", "status": "已完成",
     "desc": "DNS 解析、HTTP/HTTPS、抓包分析、网络排障"},
]

SKILLS = ["Linux", "Docker", "Nginx", "Shell", "Python", "Git",
          "阿里云", "Prometheus", "Kubernetes(学习中)", "CI/CD(学习中)"]


@app.route("/")
def index():
    return render_template("index.html", notes=NOTES, skills=SKILLS,
                           year=datetime.now().year)


if __name__ == "__main__":
    print("🖥️  http://8.147.64.234")
    print("📝  raos 的运维笔记启动")
    app.run(host="0.0.0.0", port=5000, debug=True)
