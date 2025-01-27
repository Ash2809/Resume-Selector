from src.skill_extraction import extract_skills_from_job_description2
import re

def parse_job_description(job_description):

    jd_skills = extract_skills_from_job_description2(job_description)
    print(jd_skills)
    experience_pattern = r"(\d+)\s*(?:years|yrs)?\s*(?:experience|exp)?"
    match = re.search(experience_pattern, job_description, re.IGNORECASE)
    experience = int(match.group(1)) if match else 0
    return {
        "text": job_description,
        "skills": jd_skills,
        "experience": experience
    }

if __name__ == "__main__":
    jd = """
        Job Title: Mid-Level IT Engineer
    Location: [Specify Location]
    Employment Type: Full-Time
    Experience Level: 3-5 years

    Job Summary:
    We are seeking a skilled and motivated Mid-Level IT Engineer to join our dynamic team. The ideal candidate will play a key role in maintaining and improving our IT infrastructure, ensuring optimal system performance, and contributing to the development and deployment of innovative solutions. You will work closely with cross-functional teams to support both internal and external technology needs.

    Key Responsibilities:
    System Administration:

    Install, configure, and maintain operating systems, hardware, and software.
    Manage virtualized environments using tools like VMware or Hyper-V.
    Monitor system performance and ensure system availability and reliability.
    Network Management:

    Configure, monitor, and troubleshoot network devices (e.g., routers, switches, firewalls).
    Ensure network security and compliance with best practices.
    Support VPN, WAN/LAN configurations, and cloud networking solutions.
    IT Support:

    Provide Level 2 and Level 3 technical support to resolve escalated issues.
    Collaborate with helpdesk and IT support teams to resolve complex problems.
    Project Management:

    Participate in IT infrastructure upgrades, migrations, and other projects.
    Assist in planning, scheduling, and implementing IT projects.
    Security and Compliance:

    Monitor systems for security vulnerabilities and implement solutions.
    Ensure adherence to organizational IT policies and industry compliance standards.
    Documentation and Reporting:

    Maintain accurate records of systems, configurations, and procedures.
    Prepare reports on IT system performance and resource utilization.
    Required Skills and Qualifications:
    Education: Bachelor’s degree in Computer Science, Information Technology, or related field.
    Experience: 3-5 years of hands-on experience in IT engineering or similar roles.
    Technical Skills:
    Proficiency in Windows/Linux operating systems.
    Experience with cloud platforms such as AWS, Azure, or Google Cloud.
    Familiarity with scripting languages like Python, Bash, or PowerShell.
    Strong understanding of networking protocols (e.g., TCP/IP, DNS, DHCP).
    Knowledge of ITSM tools (e.g., ServiceNow, JIRA).
    Experience with database management (SQL or NoSQL databases).
    Soft Skills:
    Excellent problem-solving and analytical skills.
    Strong communication and interpersonal skills.
    Ability to work independently and within a team.
    Strong organizational and multitasking abilities.
    Preferred Qualifications:
    Relevant certifications such as CompTIA Network+, CCNA, AWS Certified Solutions Architect, or Microsoft Azure Administrator.
    Experience with DevOps practices and tools (e.g., Docker, Kubernetes, Jenkins).
    Knowledge of ITIL framework and processes.
    Familiarity with cybersecurity principles and tools.
"""

    res = parse_job_description(jd)
    print(res["experience"])

