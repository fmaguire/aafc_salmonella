#!/usr/bin/Rscript

sir <- read.csv('ast_sir_labels.csv')
# drop the index column
sir <- sir[, !(names(sir) %in% "ID")]

pdf(file="upsetallast.pdf", onefile=FALSE)
UpSetR::upset(sir, nsets=12, order.by='freq',  mainbar.y.label = 'Set Frequency', sets.bar.color = "#56B4E9", mb.ratio = c(0.55, 0.45), sets.x.label = "Phenotypic AMR in all Serovars")
dev.off()

# not resistance
enter = subset(sir, Serovar == 'Enteriditis')
hadar = subset(sir, Serovar == 'Hadar')
heidel = subset(sir, Serovar == 'Heidelberg')
kentucky = subset(sir, Serovar == 'Kentucky')
typh = subset(sir, Serovar == 'Typhimurium')

enterica = subset(sir, Serovar == 'I:4,[5],12:i:')
# only 1 example so meaningless
thompson = subset(sir, Serovar == 'Thompson')

pdf(file="upset_hadar_ast.pdf", onefile=FALSE)
UpSetR::upset(hadar, nsets=12, order.by='freq',  mainbar.y.label = 'Set Frequency', sets.bar.color = "#de8f05", mb.ratio = c(0.55, 0.45), sets.x.label = "Hadar Resistances")
dev.off()

pdf(file='upset_heidelberg_ast.pdf', onefile=FALSE)
UpSetR::upset(heidel, nsets=12, order.by='freq',  mainbar.y.label = 'Set Frequency', sets.bar.color = "#029e73", mb.ratio = c(0.55, 0.45), sets.x.label = "Heidelberg Resistances")
dev.off()

pdf(file='upset_kentucky_ast.pdf', onefile=FALSE)
UpSetR::upset(kentucky, nsets=12, order.by='freq',  mainbar.y.label = 'Set Frequency', sets.bar.color = "#0173b2", mb.ratio = c(0.55, 0.45), sets.x.label = "Kentucky Resistances")
dev.off()

pdf(file='upset_typhimurium_ast.pdf', onefile=FALSE)
UpSetR::upset(typh, nsets=12, order.by='freq',  mainbar.y.label = 'Set Frequency', sets.bar.color = "#ca9161", mb.ratio = c(0.55, 0.45), sets.x.label = "Typhimurium Resistances")
dev.off()

pdf(file='upset_enterica_ast.pdf', onefile=FALSE)
UpSetR::upset(enterica, nsets=12, order.by='freq',  mainbar.y.label = 'Set Frequency', sets.bar.color = "#d55ee00", mb.ratio = c(0.55, 0.45), sets.x.label = "enterica I:4,[5],12:i: Resistances")
dev.off()
