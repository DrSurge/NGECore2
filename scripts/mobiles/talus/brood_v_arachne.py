import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('brood V arachne')
	mobileTemplate.setLevel(42)
	mobileTemplate.setMinLevel(42)
	mobileTemplate.setMaxLevel(42)
	mobileTemplate.setDifficulty(0)
	mobileTemplate.setAttackRange(5)
	mobileTemplate.setAttackSpeed(1.0)
	mobileTemplate.setWeaponType(6)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1.75)
	mobileTemplate.setSocialGroup("brood arachne")
	mobileTemplate.setAssistRange(12)
	mobileTemplate.setStalker(True)
	mobileTemplate.setOptionsBitmask(192)
	
	templates = Vector()
	templates.add('object/mobile/shared_angler_hue.iff')
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', 6, 1.0)
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('brood_v_arachne', mobileTemplate)
	return