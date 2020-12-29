ENV["GKSwstype"]=100  # ENV["GKSwstype"]="nul"
using Plots

gr();

plot([sin,cos],-pi,15);

#=
# %%

pyplot();

plot(sin, -pi:0.01:pi);
=#
