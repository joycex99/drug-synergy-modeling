from cruzdb import Genome

file_in = "methylation_loci.csv"
file_out = "results.csv"


f = open(file_in,'r')
hg38 = Genome('hg38')
line2g_38={}


for line in f:
        chrom, posns = line.split(":")
        start, end = map(int, posns.rstrip("|").split("-"))
        genes_38 = hg38.bin_query('refGene', chrom, start, end)

        for g in genes_38:
                line2g_38[line.strip().split(",")[0]]=g.name2
f.close()



f = open(file_in,'r')
fout = open(file_out,'w')

fout.write("loci,grch38_gene_name\n")
for line in f:
	entry = line.strip().split(",")[0]
	fout.write(entry+",")

	if entry in line2g_38:
		fout.write(line2g_38.get(entry)+"\n")
	else:
		fout.write("NA\n")

fout.close()
f.close()
