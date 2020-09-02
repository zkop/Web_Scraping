import markdown

md = markdown.Markdown()
with open("new_file.html", "w+") as file:
  file.write(md.convert("# sample heading text"))
