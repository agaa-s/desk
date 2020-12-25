ENV["GKSwstype"]=100  # ENV["GKSwstype"]="nul"
using Plots

gr();

plot([sin,cos],-pi,pi);

#=
# %%

pyplot();

plot(sin, -pi:0.01:pi);
=#
