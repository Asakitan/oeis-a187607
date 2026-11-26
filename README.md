# A187607：非对称准象的三个落点

**Chain.Ren · 独立研究** · 2026-11-27 · [公开版本 proof-v1.0.0](https://github.com/Asakitan/oeis-a187607/releases/tag/proof-v1.0.0)

在矩形棋盘上，有序三格路径数等于横、纵两轴合法走法数的乘积。取正方形，从边长 4 起计数恰为 $(4n-10)^2$。这一分解给出 [OEIS A187607](https://oeis.org/A187607) 所列的生成函数和递推。

[完整证明](PROOF.md) · [固定版本证明](https://github.com/Asakitan/oeis-a187607/blob/proof-v1.0.0/PROOF.md) · [引用资料](CITATION.cff) · [MIT 许可证](LICENSE)

复核（Python 3 标准库）：

```shell
python -B verify.py
```
