using TestImages
using Plots

# 画像の場所
# /home/kunihiko/.julia/artifacts/dd57ad5ce3051ad646bfc799a626a0048015d9a2

cameraman=testimage("cameraman");
lena=testimage("lena_color_512");
p1 = plot(cameraman);
p2 = plot(lena);
plot(p1, p2, layout = (1, 2), size = (600, 300))
