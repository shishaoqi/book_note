https://github.com/yiisoft/yii2-app-advanced/blob/master/docs/guide-zh-CN/start-installation.md

1. 下载安装yii2
	使用Composer安装
	`composer create-project --prefer-dist yiisoft/yii2-app-advanced yii-application`
	
	使用 Git 保存起最初始的文件状态

2. 初始化 -- 打开控制台终端，执行 `init` 命令并选择 `dev` 作为环境
```shell
# php /www/yii-application/init
Yii Application Initialization Tool v1.0

Which environment do you want the application to be initialized in?

  [0] Development
  [1] Production

  Your choice [0-1, or "q" to quit] 0

  Initialize the application under 'Development' environment? [yes|no] yes

  Start initialization ...

   generate frontend/config/test-local.php
   generate frontend/config/params-local.php
   generate frontend/config/main-local.php
   generate frontend/config/codeception-local.php
   generate frontend/web/index.php
   generate frontend/web/robots.txt
   generate frontend/web/index-test.php
   generate yii
   generate backend/config/test-local.php
   generate backend/config/params-local.php
   generate backend/config/main-local.php
   generate backend/config/codeception-local.php
   generate backend/web/index.php
   generate backend/web/robots.txt
   generate backend/web/index-test.php
   generate common/config/test-local.php
   generate common/config/params-local.php
   generate common/config/main-local.php
   generate common/config/codeception-local.php
   generate yii_test.bat
   generate yii_test
   generate console/config/test-local.php
   generate console/config/params-local.php
   generate console/config/main-local.php
   generate cookie validation key in backend/config/main-local.php
   generate cookie validation key in common/config/codeception-local.php
   generate cookie validation key in frontend/config/main-local.php
      chmod 0777 backend/runtime
      chmod 0777 backend/web/assets
      chmod 0777 console/runtime
      chmod 0777 frontend/runtime
      chmod 0777 frontend/web/assets
      chmod 0755 yii
      chmod 0755 yii_test

  ... initialization completed.
```
`git status` 查看结果，文件没变动

3. 1. 创建数据库 yii2advanced，并相应地调整 `common/config/main-local.php` 中的 `components['db']` 配置。
    
    打开控制台终端，执行迁移命令 php /www/yii-application/yii migrate
    执行命令后，报错：
```
# php /www/yii-application/yii migrate
Composer detected issues in your platform:

Your Composer dependencies require a PHP version ">= 8.1.0". You are running 7.4.33.
```
	解决方法：
```
# composer require "php:8.1" --dry-run

Composer could not detect the root package (yiisoft/yii2-app-advanced) version, defaulting to '1.0.0'. See https://getcomposer.org/root-version
The "8.1" constraint for "php" appears too strict and will likely not match what you want. See https://getcomposer.org/constraints
./composer.json has been updated
Composer could not detect the root package (yiisoft/yii2-app-advanced) version, defaulting to '1.0.0'. See https://getcomposer.org/root-version
Running composer update php
Loading composer repositories with package information
Updating dependencies
Your requirements could not be resolved to an installable set of packages.

  Problem 1
    - Root composer.json requires php 8.1 (exact version match: 8.1, 8.1.0 or 8.1.0.0) but your php version (7.4.33) does not satisfy that requirement.
  Problem 2
    - codeception/codeception is locked to version 5.2.2 and an update of this package was not requested.
    - codeception/codeception 5.2.2 requires php ^8.1 -> your php version (7.4.33) does not satisfy that requirement.
  Problem 3
    - codeception/lib-innerbrowser is locked to version 3.1.3 and an update of this package was not requested.
    - codeception/lib-innerbrowser 3.1.3 requires php ^8.0 -> your php version (7.4.33) does not satisfy that requirement.
  Problem 4
    - codeception/module-asserts is locked to version 3.0.0 and an update of this package was not requested.
    - codeception/module-asserts 3.0.0 requires php ^8.0 -> your php version (7.4.33) does not satisfy that requirement.
  Problem 5
    - codeception/module-yii2 is locked to version 1.1.12 and an update of this package was not requested.
    - codeception/module-yii2 1.1.12 requires php ^8.0 -> your php version (7.4.33) does not satisfy that requirement.
  Problem 6
    - codeception/module-filesystem is locked to version 3.0.0 and an update of this package was not requested.
    - codeception/module-filesystem 3.0.0 requires php ^8.0 -> your php version (7.4.33) does not satisfy that requirement.
  Problem 7
    - symfony/browser-kit is locked to version v6.4.19 and an update of this package was not requested.
    - symfony/browser-kit v6.4.19 requires php >=8.1 -> your php version (7.4.33) does not satisfy that requirement.
  Problem 8
    - symfony/mailer v6.4.21 requires php >=8.1 -> your php version (7.4.33) does not satisfy that requirement.
    - yiisoft/yii2-symfonymailer 2.0.4 requires symfony/mailer >=5.4.0 -> satisfiable by symfony/mailer[v6.4.21].
    - yiisoft/yii2-symfonymailer is locked to version 2.0.4 and an update of this package was not requested.


Installation failed, reverting ./composer.json and ./composer.lock to their original content.
```

修改 composer.json 文件，得以解决，详情看 git log 日志记录。

