import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('heroic_tusken_mos_espa_citizen')
	mobileTemplate.setLevel(90)
	mobileTemplate.setDifficulty(0)
	mobileTemplate.setAttackRange(12)
	mobileTemplate.setAttackSpeed(1.0)
	mobileTemplate.setWeaponType(6)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(True)
	mobileTemplate.setScale(1)
	mobileTemplate.setSocialGroup("heroic mos espa citizien")
	mobileTemplate.setAssistRange(12)
	mobileTemplate.setStalker(True)
	mobileTemplate.setOptionsBitmask(128)
	
	templates = Vector()
	templates.add('object/mobile/shared_warren_research_scientist.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_female_06.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_male_05.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_nikto_male_06.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_rodian_female_04.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_devaronian_male_03.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_sullustan_male_03.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_female_02.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_male_01.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_male_08.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_bith_female_03.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_bith_male_04.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_ishitib_male_02.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_male_08.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_nikto_male_02.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_rodian_male_01.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_trandoshan_female_02.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_female_07.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_male_04.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_bith_male_01.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_trandoshan_male_02.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_bith_female_06.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_nikto_male_07.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_rodian_male_04.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_sullustan_male_02.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_female_03.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_bith_male_05.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_devaronian_male_02.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_ishitib_male_03.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_nikto_male_03.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_rodian_female_01.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_trandoshan_female_03.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_male_09.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_bith_female_02.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_sullustan_male_06.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_devaronian_male_01.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_sullustan_male_01.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_female_04.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_male_07.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_bith_female_05.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_bith_male_02.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_nikto_male_04.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_trandoshan_female_04.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_rodian_female_02.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_sullustan_male_05.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_male_03.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_bith_female_01.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_bith_male_06.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_rodian_male_03.iff')	
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_male_06.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_bith_male_03.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_nikto_male_05.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_female_05.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_bith_female_04.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_trandoshan_male_01.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_sullustan_male_04.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_devaronian_male_04.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_male_02.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_ishitib_male_01.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_female_01.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_nikto_male_01.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_rodian_female_03.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_trandoshan_female_01.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_aqualish_female_08.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_nikto_male_08.iff')
	templates.add('object/mobile/shared_dressed_commoner_tatooine_rodian_male_02.iff')
	templates.add('object/mobile/shared_dressed_twi_female_scientist_01.iff')
	templates.add('object/mobile/shared_warren_scientist_s01.iff')
	
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', 6, 1.0)
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)

	attacks = Vector()
	mobileTemplate.setDefaultAttack('meleeHit')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('heroic_mos_espa_citizen', mobileTemplate)
	return