from axju.contrib import resume

class AxJu(resume.Resume):
    """The resume from Axel Juraske"""

    me = resume.Person(name="Axel", lastname="Juraske", email="axel.juraske@short-report.de")

    short = resume.Project(name="Short-report", description="My first blog")
    socialpy = resume.Project(name="SocialPy", description="A gateway tosocial networks")
