# UTF-8：编码、解码与校验

多语言文本编码后字节数不对、截断数据没报错：码点没有按长度分段，解码没有看首字节，续字节没有校验，非法序列漏过，字符串编码没拼接，空输入崩，批量转换只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
codec/__init__.py
codec/utf8.py
tests/test_utf8.py
```

## 当前状态

`codec/utf8.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_utf8.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 码点按长度分段
2. 解码看首字节
3. 续字节校验
4. 非法序列拒绝
5. 字符串拼接
6. 空输入兜底

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `codec/utf8.py`
后 15 条用例应全部通过。
