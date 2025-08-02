#!/usr/bin/env python3

import os
import re

def update_individual_pages():
    """Update all individual pages with correct relative paths and navigation"""
    
    # Update travel pages
    travel_files = [
        'travels/lofotenIslands.html',
        'travels/montBlanc.html', 
        'travels/fiveHundredMilesToBilboa.html',
        'travels/athensToVenice.html',
        'travels/tahitianPearlFarming.html',
        'travels/scandinaviaByTrain.html'
    ]
    
    for file_path in travel_files:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Update navigation links to use correct relative paths
            content = re.sub(r'href="index\.html"', 'href="../index.html"', content)
            content = re.sub(r'href="travels\.html"', 'href="../travels.html"', content)
            content = re.sub(r'href="articles\.html"', 'href="../articles.html"', content)
            content = re.sub(r'href="projects\.html"', 'href="../projects.html"', content)
            content = re.sub(r'href="cv\.html"', 'href="../cv.html"', content)
            content = re.sub(r'href="contact\.html"', 'href="../contact.html"', content)
            
            # Update dropdown links
            content = re.sub(r'href="travels/lofotenIslands\.html"', 'href="lofotenIslands.html"', content)
            content = re.sub(r'href="travels/montBlanc\.html"', 'href="montBlanc.html"', content)
            content = re.sub(r'href="travels/fiveHundredMilesToBilboa\.html"', 'href="fiveHundredMilesToBilboa.html"', content)
            content = re.sub(r'href="travels/athensToVenice\.html"', 'href="athensToVenice.html"', content)
            content = re.sub(r'href="travels/tahitianPearlFarming\.html"', 'href="tahitianPearlFarming.html"', content)
            content = re.sub(r'href="travels/scandinaviaByTrain\.html"', 'href="scandinaviaByTrain.html"', content)
            
            content = re.sub(r'href="articles/krushnicEffectEPQ\.html"', 'href="../articles/krushnicEffectEPQ.html"', content)
            content = re.sub(r'href="articles/riskAndOpportunityCost\.html"', 'href="../articles/riskAndOpportunityCost.html"', content)
            content = re.sub(r'href="articles/misleadingScalingLawsOfAI\.html"', 'href="../articles/misleadingScalingLawsOfAI.html"', content)
            content = re.sub(r'href="articles/exponentialGrowthAndInequality\.html"', 'href="../articles/exponentialGrowthAndInequality.html"', content)
            content = re.sub(r'href="articles/caseForNuclearPower\.html"', 'href="../articles/caseForNuclearPower.html"', content)
            content = re.sub(r'href="articles/georgismInModernWorld\.html"', 'href="../articles/georgismInModernWorld.html"', content)
            
            content = re.sub(r'href="projects/tutoringWebsite\.html"', 'href="../projects/tutoringWebsite.html"', content)
            content = re.sub(r'href="projects/programmableSmartCharger\.html"', 'href="../projects/programmableSmartCharger.html"', content)
            
            # Update CSS and JS paths
            content = re.sub(r'href="assets/css/style\.css"', 'href="../assets/css/style.css"', content)
            content = re.sub(r'src="assets/js/script\.js"', 'src="../assets/js/script.js"', content)
            
            # Update image paths
            content = re.sub(r'src="assets/images/', 'src="../assets/images/', content)
            
            with open(file_path, 'w') as f:
                f.write(content)
            
            print(f"Updated {file_path}")
    
    # Update article pages
    article_files = [
        'articles/krushnicEffectEPQ.html',
        'articles/riskAndOpportunityCost.html',
        'articles/misleadingScalingLawsOfAI.html',
        'articles/exponentialGrowthAndInequality.html',
        'articles/caseForNuclearPower.html',
        'articles/georgismInModernWorld.html'
    ]
    
    for file_path in article_files:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Update navigation links to use correct relative paths
            content = re.sub(r'href="index\.html"', 'href="../index.html"', content)
            content = re.sub(r'href="travels\.html"', 'href="../travels.html"', content)
            content = re.sub(r'href="articles\.html"', 'href="../articles.html"', content)
            content = re.sub(r'href="projects\.html"', 'href="../projects.html"', content)
            content = re.sub(r'href="cv\.html"', 'href="../cv.html"', content)
            content = re.sub(r'href="contact\.html"', 'href="../contact.html"', content)
            
            # Update dropdown links
            content = re.sub(r'href="travels/lofotenIslands\.html"', 'href="../travels/lofotenIslands.html"', content)
            content = re.sub(r'href="travels/montBlanc\.html"', 'href="../travels/montBlanc.html"', content)
            content = re.sub(r'href="travels/fiveHundredMilesToBilboa\.html"', 'href="../travels/fiveHundredMilesToBilboa.html"', content)
            content = re.sub(r'href="travels/athensToVenice\.html"', 'href="../travels/athensToVenice.html"', content)
            content = re.sub(r'href="travels/tahitianPearlFarming\.html"', 'href="../travels/tahitianPearlFarming.html"', content)
            content = re.sub(r'href="travels/scandinaviaByTrain\.html"', 'href="../travels/scandinaviaByTrain.html"', content)
            
            content = re.sub(r'href="articles/krushnicEffectEPQ\.html"', 'href="krushnicEffectEPQ.html"', content)
            content = re.sub(r'href="articles/riskAndOpportunityCost\.html"', 'href="riskAndOpportunityCost.html"', content)
            content = re.sub(r'href="articles/misleadingScalingLawsOfAI\.html"', 'href="misleadingScalingLawsOfAI.html"', content)
            content = re.sub(r'href="articles/exponentialGrowthAndInequality\.html"', 'href="exponentialGrowthAndInequality.html"', content)
            content = re.sub(r'href="articles/caseForNuclearPower\.html"', 'href="caseForNuclearPower.html"', content)
            content = re.sub(r'href="articles/georgismInModernWorld\.html"', 'href="georgismInModernWorld.html"', content)
            
            content = re.sub(r'href="projects/tutoringWebsite\.html"', 'href="../projects/tutoringWebsite.html"', content)
            content = re.sub(r'href="projects/programmableSmartCharger\.html"', 'href="../projects/programmableSmartCharger.html"', content)
            
            # Update CSS and JS paths
            content = re.sub(r'href="assets/css/style\.css"', 'href="../assets/css/style.css"', content)
            content = re.sub(r'src="assets/js/script\.js"', 'src="../assets/js/script.js"', content)
            
            # Update image paths
            content = re.sub(r'src="assets/images/', 'src="../assets/images/', content)
            
            with open(file_path, 'w') as f:
                f.write(content)
            
            print(f"Updated {file_path}")
    
    # Update project pages
    project_files = [
        'projects/tutoringWebsite.html',
        'projects/programmableSmartCharger.html'
    ]
    
    for file_path in project_files:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Update navigation links to use correct relative paths
            content = re.sub(r'href="index\.html"', 'href="../index.html"', content)
            content = re.sub(r'href="travels\.html"', 'href="../travels.html"', content)
            content = re.sub(r'href="articles\.html"', 'href="../articles.html"', content)
            content = re.sub(r'href="projects\.html"', 'href="../projects.html"', content)
            content = re.sub(r'href="cv\.html"', 'href="../cv.html"', content)
            content = re.sub(r'href="contact\.html"', 'href="../contact.html"', content)
            
            # Update dropdown links
            content = re.sub(r'href="travels/lofotenIslands\.html"', 'href="../travels/lofotenIslands.html"', content)
            content = re.sub(r'href="travels/montBlanc\.html"', 'href="../travels/montBlanc.html"', content)
            content = re.sub(r'href="travels/fiveHundredMilesToBilboa\.html"', 'href="../travels/fiveHundredMilesToBilboa.html"', content)
            content = re.sub(r'href="travels/athensToVenice\.html"', 'href="../travels/athensToVenice.html"', content)
            content = re.sub(r'href="travels/tahitianPearlFarming\.html"', 'href="../travels/tahitianPearlFarming.html"', content)
            content = re.sub(r'href="travels/scandinaviaByTrain\.html"', 'href="../travels/scandinaviaByTrain.html"', content)
            
            content = re.sub(r'href="articles/krushnicEffectEPQ\.html"', 'href="../articles/krushnicEffectEPQ.html"', content)
            content = re.sub(r'href="articles/riskAndOpportunityCost\.html"', 'href="../articles/riskAndOpportunityCost.html"', content)
            content = re.sub(r'href="articles/misleadingScalingLawsOfAI\.html"', 'href="../articles/misleadingScalingLawsOfAI.html"', content)
            content = re.sub(r'href="articles/exponentialGrowthAndInequality\.html"', 'href="../articles/exponentialGrowthAndInequality.html"', content)
            content = re.sub(r'href="articles/caseForNuclearPower\.html"', 'href="../articles/caseForNuclearPower.html"', content)
            content = re.sub(r'href="articles/georgismInModernWorld\.html"', 'href="../articles/georgismInModernWorld.html"', content)
            
            content = re.sub(r'href="projects/tutoringWebsite\.html"', 'href="tutoringWebsite.html"', content)
            content = re.sub(r'href="projects/programmableSmartCharger\.html"', 'href="programmableSmartCharger.html"', content)
            
            # Update CSS and JS paths
            content = re.sub(r'href="assets/css/style\.css"', 'href="../assets/css/style.css"', content)
            content = re.sub(r'src="assets/js/script\.js"', 'src="../assets/js/script.js"', content)
            
            # Update image paths
            content = re.sub(r'src="assets/images/', 'src="../assets/images/', content)
            
            with open(file_path, 'w') as f:
                f.write(content)
            
            print(f"Updated {file_path}")

if __name__ == "__main__":
    update_individual_pages() 