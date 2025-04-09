#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import re
import sys

def run_command(command):
    """运行shell命令并返回输出"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"命令执行错误: {e}")
        return None

def get_active_network_service():
    """获取当前活跃的网络服务"""
    output = run_command("networksetup -listallnetworkservices")
    if not output:
        return None
    
    # 获取所有网络服务（跳过第一行，因为它是标题）
    services = output.split('\n')[1:]
    
    # 过滤掉被禁用的服务（带有*号的服务）
    active_services = [service for service in services if not service.startswith('*')]
    
    if active_services:
        return active_services[0]  # 返回第一个活跃的服务
    return None

def check_proxy_status(service):
    """检查指定网络服务的代理设置状态"""
    if not service:
        print("未找到活跃的网络服务")
        return
    
    print(f"正在检查网络服务 '{service}' 的代理设置...\n")
    
    # 检查自动发现代理
    auto_discovery = run_command(f"networksetup -getproxyautodiscovery '{service}'")
    print(f"自动发现代理详细信息:\n{auto_discovery}")
    auto_discovery_enabled = "已启用" if ("已启用" in auto_discovery) or ("Enabled: Yes" in auto_discovery) else "已禁用"
    print(f"自动发现代理状态: {auto_discovery_enabled}\n")
    
    # 检查自动配置代理
    auto_proxy = run_command(f"networksetup -getautoproxyurl '{service}'")
    print(f"自动配置代理详细信息:\n{auto_proxy}")
    auto_proxy_enabled = "已启用" if ("已启用" in auto_proxy) or ("Enabled: Yes" in auto_proxy) else "已禁用"
    print(f"自动配置代理状态: {auto_proxy_enabled}\n")
    
    # 检查HTTP代理
    http_proxy = run_command(f"networksetup -getwebproxy '{service}'")
    print(f"网页代理(HTTP)详细信息:\n{http_proxy}")
    http_proxy_enabled = "已启用" if ("已启用" in http_proxy) or ("Enabled: Yes" in http_proxy) else "已禁用"
    print(f"网页代理(HTTP)状态: {http_proxy_enabled}\n")
    
    # 检查HTTPS代理
    https_proxy = run_command(f"networksetup -getsecurewebproxy '{service}'")
    print(f"安全网页代理(HTTPS)详细信息:\n{https_proxy}")
    https_proxy_enabled = "已启用" if ("已启用" in https_proxy) or ("Enabled: Yes" in https_proxy) else "已禁用"
    print(f"安全网页代理(HTTPS)状态: {https_proxy_enabled}\n")
    
    # 检查SOCKS代理
    socks_proxy = run_command(f"networksetup -getsocksfirewallproxy '{service}'")
    print(f"SOCKS代理详细信息:\n{socks_proxy}")
    socks_proxy_enabled = "已启用" if ("已启用" in socks_proxy) or ("Enabled: Yes" in socks_proxy) else "已禁用"
    print(f"SOCKS代理状态: {socks_proxy_enabled}")

def main():
    print("Mac代理设置检查工具")
    print("-" * 30)
    
    # 获取当前活跃的网络服务
    active_service = get_active_network_service()
    
    # 检查代理状态
    check_proxy_status(active_service)

if __name__ == "__main__":
    main()
