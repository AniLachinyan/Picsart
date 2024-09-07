def generate_report(title, author, content, *, summary=None, conclusion=None):
    report= f"Title: {title}\n"
    report+= f"Author: {author}\n"
    report+= f"Content: {content}\n"
    if (summary!=None):
        report+= f"Summary:\n{summary}\n"
    if (conclusion!=None):
        report+= f"Conclusion:\n{conclusion}"
    return report    
print(generate_report("Annual Report", "John Doe", "This is the main content of the report.", summary="This report covers the annual performance.", conclusion="The company has had a successful year."))
        
