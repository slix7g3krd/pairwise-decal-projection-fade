# pairwise-decal-projection-fade

## 领域

游戏、图形与多媒体

## 主题

贴花投影与深度

## 说明

切线空间投射、可见性淘汰与法线跟随。

初始状态下 `graphics/decal_projection_fade.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
