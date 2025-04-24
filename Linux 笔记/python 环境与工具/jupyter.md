
### 启动，加无ip限制
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser

### 报错
1. Jupyter command `jupyter-lab` not found. ---- pip install jupyterlab

conda create --name xxx python=3.10
conda activate xxx

pip install jupyterlab
conda install ipython
conda install ipykernel
python -m ipykernel install --user --name=xxx --display-name="xxxx"


### 要将Conda创建的环境添加到Jupyter的“Select kernel”选项中
要将Conda创建的环境添加到Jupyter的“Select kernel”选项中，您需要确保该环境中安装了IPython。以下是详细步骤：

1. **激活Conda环境**：
   使用以下命令激活您创建的Conda环境：
   ```bash
   conda activate myenv
   ```

2. **安装IPython**：
   在激活的环境中安装IPython。这将确保环境具有Jupyter所需的内核：
   ```bash
   conda install ipython
   ```

3. **安装ipykernel**：
   接下来，安装`ipykernel`，这是一个轻量级的IPython内核，用于Jupyter：
   ```bash
   conda install ipykernel
   ```

4. **注册内核**：
   使用`ipykernel`注册您的Conda环境作为Jupyter内核：
   ```bash
   python -m ipykernel install --user --name=myenv --display-name="Python (myenv)"
   ```
   这里 `myenv` 是您的环境名称，`--display-name` 是在Jupyter中显示的名称。

5. **检查内核**：
   在Jupyter中检查新注册的内核是否可用。启动Jupyter Notebook或JupyterLab，然后在“Select kernel”下拉菜单中查找新添加的内核。

6. **重新启动Jupyter**：
   如果您在添加内核后没有看到新选项，尝试重新启动Jupyter Notebook或JupyterLab。

7. **使用新内核**：
   在Jupyter界面中选择新注册的内核，然后开始在该环境中运行代码。

8. **检查环境变量**：
   如果内核没有正确注册，检查环境变量是否设置正确，特别是`PYTHONPATH`。

9. **检查Jupyter配置**：
   确保Jupyter配置没有阻止新内核的注册或显示。

10. **考虑使用Conda环境中的Jupyter**：
    如果您在Conda环境中工作，可以考虑使用该环境中的Jupyter安装版本，以确保所有路径和依赖项都正确设置。

请注意，如果您使用的是虚拟环境，建议在该环境中安装Jupyter，以确保所有依赖项都与您的项目环境一致。您可以通过在激活的环境中运行`conda install jupyter`或`pip install notebook`来安装Jupyter。
