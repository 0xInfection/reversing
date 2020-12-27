from bs4 import BeautifulSoup

htm = '''
<!DOCTYPE html><html lang="en"><head><meta name="pageKey" content="d_flagship2_pulse_read"><meta name="linkedin:pageTag" content="old=index;new=index"><meta name="locale" content="en_US"><meta id="config"data-app-id=""data-custom-tracking-code=""data-tracking-page-type=""/><meta id="google-analytics-config"data-use-location-for-dp=""data-use-page-title=""/><link rel="canonical" href="https://www.linkedin.com/pulse/assembly-language-basic-malware-reverse-engineering-kevin-m-thomas"><link rel="manifest" href="/homepage-guest/manifest.json" crossorigin="use-credentials"/><link rel="icon" href="https://static-exp1.licdn.com/scds/common/u/images/logos/favicons/v1/favicon.ico"><script>function getDfd() {let yFn,nFn;const p=new Promise((y, n)=>{yFn=y;nFn=n;});p.resolve=yFn;p.reject=nFn;return p;}window.lazyloader = getDfd();window.tracking = getDfd();window.impressionTracking = getDfd();window.ingraphTracking = getDfd();window.appDetection = getDfd();</script><title>Assembly Language - Basic Malware Reverse Engineering (Part 1:  Goals)</title><meta name="robots" content="noarchive"><meta name="description" content="For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github."><meta name="google-site-verification" content="t9M-lk-kbgtImg1_i_dtbW8DnGO0ZEzvRHHv7pcJoZA"/><meta property="og:title" content="Assembly Language - Basic Malware Reverse Engineering (Part 1:  Goals)" /><meta property="og:description" content="For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github." /><meta property="og:image" content="https://media-exp1.licdn.com/dms/image/C4E12AQFHb7sY3kQ_1w/article-cover_image-shrink_600_2000/0/1520170138889?e=1614816000&amp;v=beta&amp;t=ke8dgzkoUWnCXX4DjrlWyn9pKVvKTs9dIz0EOoWfDFo" /><meta property="og:url" content="https://www.linkedin.com/pulse/assembly-language-basic-malware-reverse-engineering-kevin-m-thomas" /><meta property="og:type" content="website" /><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@LinkedInEditors"><meta name="twitter:title" content="Assembly Language - Basic Malware Reverse Engineering (Part 1:  Goals)"><meta name="twitter:description" content="For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github."><meta name="fb:app_id" content="161320853908703"><meta name="clientSideIngraphs" content="1" data-gauge-metric-endpoint="/content-guest/api/ingraphs/gauge" data-counter-metric-endpoint="/content-guest/api/ingraphs/counter"/><link rel="stylesheet" href="https://static-exp1.licdn.com/sc/h/1waqcoh4yb3k9qsf8rlntd926"/></head><body><form class="google-one-tap" action="https://www.linkedin.com/uas/login-submit" method="post"><input type="hidden" name="loginCsrfParam" value="088c0057-78a7-4092-838b-707649cfadf0"/><input type="hidden" name="session_redirect" value="https://www.linkedin.com/today/author/mytechnotalent" /><input type="hidden" name="trk" value="article_google-one-tap-submit"/><div id="google-one-tap__container" class="google-one-tap__container" data-tracking-control-name="article_google-one-tap"></div><div class="loader loader--full-screen"><div class="loader__container"><icon class="loader__icon loader__icon--default"data-delayed-url="https://static-exp1.licdn.com/sc/h/ddi43qwelxeqjxdd45pe3fvs1"data-svg-class-name="loader__icon-svg--large"></icon></div></div></form><header class="navbar global-alert-offset"style="height:64px"><div class="navbar__wrapper "><a data-tracking-control-name="d_flagship2_pulse_read_logo" data-tracking-will-navigate href="/?trk=d_flagship2_pulse_read_logo" class="nav-header__logo-link" aria-label="LinkedIn"><icon class="nav-header__logo-icon" data-delayed-url="https://static-exp1.licdn.com/sc/h/8fkga714vy9b2wk5auqo5reeb"></icon></a><nav class="nav-header__guest-nav" aria-label="Primary"><ul class="nav-header__link-list"><li class="nav-header__link-item"><a class="nav-header__link" data-tracking-control-name="d_flagship2_pulse_read_join" data-tracking-will-navigate href="https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fpulse%2Fassembly-language-basic-malware-reverse-engineering-kevin-m-thomas&amp;trk=d_flagship2_pulse_read_join" rel="nofollow">Join now</a></li><li class="nav-header__link-item"><a class="nav-header__link-button" data-tracking-control-name="d_flagship2_pulse_read_signin" data-tracking-will-navigate href="https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fpulse%2Fassembly-language-basic-malware-reverse-engineering-kevin-m-thomas&amp;trk=d_flagship2_pulse_read_signin">Sign in</a></li></ul></nav></div></header><figure class="article-cover-image"><img alt="Assembly Language - Basic Malware Reverse Engineering (Part 1:  Goals)" class="lazy-load article-cover-image-default article-cover-image-small" data-delayed-url="https://media-exp1.licdn.com/dms/image/C4E12AQFHb7sY3kQ_1w/article-cover_image-shrink_600_2000/0/1520170138889?e=1614816000&amp;v=beta&amp;t=ke8dgzkoUWnCXX4DjrlWyn9pKVvKTs9dIz0EOoWfDFo" /></figure><div class="article-cover-image__caption"><figcaption itemprop="caption"></figcaption></div><article class="main single-col-grid article-grid" ><header class="article-head"><h1 class="article-title">Assembly Language - Basic Malware Reverse Engineering (Part 1:  Goals)</h1><time class="article-head__timestamp">Published on April 6, 2016</time><time class="article-head__mobile-timestamp">April 6, 2016&nbsp;•&nbsp;56&nbsp;Likes&nbsp;•&nbsp;0 Comments</time><div class="ellipsis-menu"><div class="collapsible-dropdown article-head__ellipsis-menu"><ul class="collapsible-dropdown__list article-head__ellipsis-menu__list hidden" role="menu"><li class="ellipsis-menu__item"><a href="https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fpulse%2Fassembly-language-basic-malware-reverse-engineering-kevin-m-thomas&amp;trk=article-head_ellipsis-menu-sign-in-redirect"class="ellipsis-menu__item-button"data-tracking-control-name="article-head_ellipsis-menu-sign-in-redirect"data-tracking-will-navigate><icon class="ellipsis-menu__item-icon"data-delayed-url="https://static-exp1.licdn.com/sc/h/43bxdx7i9x7nc4dsqaf24dop1"></icon>Report this post</a></li></ul><button class="ellipsis-menu__trigger collapsible-dropdown__button"aria-expanded="false"data-tracking-control-name="article-head_ellipsis-menu-trigger"><icon class="ellipsis-menu__trigger-icon"data-delayed-url="https://static-exp1.licdn.com/sc/h/8qp95h4fglmoykpiam2j9pxo3"/></icon></button></div></div><div class="author-info"><div data-impression-id="author_mini-profile_mini-card" class="mini-card mini-profile mini-card--flat mini-profile--flat"><img class="mini-card__image mini-profile__image mini-card__image--flat mini-profile__image--flat lazy-load"data-delayed-url="https://media-exp1.licdn.com/dms/image/C4E03AQHj9smy0fl_GA/profile-displayphoto-shrink_100_100/0/1560618806133?e=1614816000&amp;v=beta&amp;t=RpflhN90JitKOWGeZX7eoS53-f3VMPviqzm-KAwpwZg"alt="Kevin Thomas"/><section class="mini-card__content mini-profile__content mini-card__content--flat mini-profile__content--flat"><h3 class="mini-card__title mini-profile__title mini-card__title--flat mini-profile__title--flat"><a class="mini-card__title-link mini-profile__title-link mini-card__title-link--flat mini-profile__title-link--flat"data-tracking-control-name="author_mini-profile_title"data-tracking-will-navigate=""href="https://www.linkedin.com/in/mytechnotalent?trk=author_mini-profile_title"aria-label="View profile for Kevin Thomas">Kevin Thomas</a><a class="author-info__follow-button"data-tracking-will-navigate data-tracking-control-name="author-info__follow-button"href="https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fpulse%2Fassembly-language-basic-malware-reverse-engineering-kevin-m-thomas&amp;trk=author-info__follow-button">Follow</a></h3><h4 class="mini-card__subtitle mini-profile__subtitle mini-card__subtitle--flat mini-profile__subtitle--flat">Senior Software Engineer in Test at BluVector, A Comcast Company</h4></section></div><ul class="social-ctas"><li class="social-ctas__list-item"><button class="button-secondary-medium-round-muted social-ctas__button social-ctas__like-button" type="button" data-tracking-control-name="urn:li:control:d_flagship3_pulse_read-like"><li-icon aria-hidden="true" type="like-icon" class="social-ctas__button-icon"></li-icon>Like</button><span class="social-ctas__number">56</span></li><li class="social-ctas__list-item"><button class="button-secondary-medium-round-muted social-ctas__button social-ctas__comment-button" type="button" data-tracking-control-name="urn:li:control:d_flagship3_pulse_read-comment_intent"><li-icon aria-hidden="true" type="comment-icon" class="social-ctas__button-icon"></li-icon>Comment</button><span class="social-ctas__number">0</span></li><li class="social-ctas__list-item"><div data-tracking-control-name="social_share" data-share-message="Assembly Language - Basic Malware Reverse Engineering (Part 1:  Goals)"  class="social-share social-ctas__button"><input type="checkbox"role="button"class="social-share__state autoclose"data-no-close-selector=".share__list"aria-label="Show share options"aria-expanded="false"data-show-dialog-string="Show share options"data-hide-dialog-string="Hide share options"id="social-share__state-social-share-article"><label for="social-share__state-social-share-article" class="social-share__button social-share__button-circular"><icon class="social-share__button-icon lazy-load background"></icon><span class="social-share__button-text-circular">Share</span></label><ul class="social-share__options social-share__list social-share__list--bottom-left" id="social-share__dropdown"><li><button data-tracking-control-name="social_share_linkedin" class="social-share__item" data-share-service="linkedin"><icon class="social-share__item-icon"data-delayed-url="https://static-exp1.licdn.com/sc/h/64x33s3lxd27lb5jrntc2qt3s"></icon><span class="social-share__item-text">LinkedIn</span></button></li><li><button data-tracking-control-name="social_share_facebook" class="social-share__item" data-share-service="facebook"><icon class="social-share__item-icon"data-delayed-url="https://static-exp1.licdn.com/sc/h/7y4vm785suau3ad8ch5j8yq3w"></icon><span class="social-share__item-text">Facebook</span></button></li><li><button data-tracking-control-name="social_share_twitter" class="social-share__item" data-share-service="twitter"><icon class="social-share__item-icon"data-delayed-url="https://static-exp1.licdn.com/sc/h/dcsfv212z1ozhe7tgrxjrs55a"></icon><span class="social-share__item-text">Twitter</span></button></li></ul></div><span class="social-ctas__number">0</span></li></ul></div></header><section class="article-body" data-redirect-url="https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fpulse%2Fassembly-language-basic-malware-reverse-engineering-kevin-m-thomas"><p>For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial</p><p>Essential to the discussion of basic reverse engineering is the concept of modern malware analysis. Malware analysis is the understanding and examination of information necessary to respond to a network intrusion.</p><p>This short tutorial will begin with the basic concepts of malware reverse engineering and graduate to an entry-level basic examination of Assembly Language.</p><p>The keys to the kingdom so to speak are rooted in the break-down of the respective suspected malware binary and how to find it on your network and ultimately to contain it.</p><p>Upon full identification of the files required for deeper analysis, it is critical to develop signatures to detect malware infections throughout your network whether it be a home based LAN or complex corporate WAN to which malware analysis is necessary to develop host-based and network signatures.</p><p>To begin with the concept of a host-based signature, we need to understand that these are utilized to find malicious code in a target machine. Host-based signatures are also referred to as indicators which can identify files created or edited by the infected code which can make hidden changes to a computers registry. This is quite in contrast with antivirus signatures because these concentrate on what the malware actually does rather than the make-up of the malware which makes them more effective in finding malware that can migrate or has been removed from the media.</p><p>In contrast, network signatures are used to find malicious code by examining network traffic. It is important to note such tools as WireShark and the like are often effective in such analysis.</p><p>Upon identification of these aforementioned signatures, the next step is to identify what the malware is actually doing.</p><p><strong>UNDER NO CONDITIONS ARE YOU TO EVER USE THIS EDUCATION TO CAUSE HARM TO ANY SYSTEM OF ANY KIND AS I AM NOT RESPONSIBLE! THIS IS FOR LEARNING PURPOSES ONLY!</strong></p><p>In our next lesson we will discuss techniques of malware analysis.</p></section><div class="author-info author-info__container"><div data-impression-id="author_mini-profile_mini-card" class="mini-card mini-profile mini-card--flat mini-profile--flat"><img class="mini-card__image mini-profile__image mini-card__image--flat mini-profile__image--flat lazy-load"data-delayed-url="https://media-exp1.licdn.com/dms/image/C4E03AQHj9smy0fl_GA/profile-displayphoto-shrink_100_100/0/1560618806133?e=1614816000&amp;v=beta&amp;t=RpflhN90JitKOWGeZX7eoS53-f3VMPviqzm-KAwpwZg"alt="Kevin Thomas"/><section class="mini-card__content mini-profile__content mini-card__content--flat mini-profile__content--flat"><h3 class="mini-card__title mini-profile__title mini-card__title--flat mini-profile__title--flat"><a class="mini-card__title-link mini-profile__title-link mini-card__title-link--flat mini-profile__title-link--flat"data-tracking-control-name="author_mini-profile_title"data-tracking-will-navigate=""href="https://www.linkedin.com/in/mytechnotalent?trk=author_mini-profile_title"aria-label="View profile for Kevin Thomas">Kevin Thomas</a></h3><h4 class="mini-card__subtitle mini-profile__subtitle mini-card__subtitle--flat mini-profile__subtitle--flat">Senior Software Engineer in Test at BluVector, A Comcast Company</h4></section></div><a class="author-info__follow-button-bottom"data-tracking-will-navigate data-tracking-control-name="author-info__follow-button-bottom"href="https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fpulse%2Fassembly-language-basic-malware-reverse-engineering-kevin-m-thomas&amp;trk=author-info__follow-button-bottom">Follow</a></div><div class="article-comment__container" data-article-urn="urn:li:article:8070593670180647249" data-article-permalink="assembly-language-basic-malware-reverse-engineering-kevin-m-thomas"><div class="article-comment__header" data-total-comment="0">0 comments</div><div class="article-comment__guest-leave-comment"><img class="article-comment__guest-image" src="https://static-exp1.licdn.com/sc/h/efkb5179rslll10nmhystl3wx" alt="article-comment__guest-image"><div class="article-comment__guest-signin-view"><a class="article-comment__guest-leave-comment--signin" data-tracking-control-name="article-reader_guest-leave-comment" data-tracking-will-navigate href="https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fpulse%2Fassembly-language-basic-malware-reverse-engineering-kevin-m-thomas&amp;trk=article-reader_leave-comment">Sign in </a>to leave your comment</div></div><div class="article-comments-insert-slot"></div></div></article><div class="main related-articles-container"><hr/><span class="related-articles__title-container"><h3 class="related-articles__title">More from Kevin Thomas</h3><a data-tracking-will-navigate data-tracking-control-name="author-info__articles-link" href="https://www.linkedin.com/today/author/mytechnotalent?trk=author-info__article-link">216 articles</a></span><div class="related-articles "><div class="article-card"><div class="article-card__image--wrapper"><img class="lazy-load article-card__image"alt="Lesson 3: MicroPython For micro:bit (Part 3: Conditional Logic)"data-delayed-url="https://media-exp1.licdn.com/dms/image/C4E12AQF6TSZaRpPjMA/article-cover_image-shrink_720_1280/0/1608971179159?e=1614816000&amp;v=beta&amp;t=-Jtpttyy4Yg4SpsVA_RuaB5EMNyzzDG8Mccfb1lW3a4"/></div><div class="article-card__content"><h3 class="article-card__title"><a class="article-card__title--link"href="/pulse/lesson-3-micropython-microbit-part-conditional-logic-kevin-thomas?trk=read_related_article-card_title"data-tracking-control-name="read_related_article-card_title"data-tracking-will-navigate>Lesson 3: MicroPython For micro:bit (Part 3:…</a></h3><p class="article-card__meta-info"><span class="article-card__meta-info-item">December 26, 2020</span></p> <p class="article-card__meta-info article-card__meta-info--counts"></p></div></div><div class="article-card"><div class="article-card__image--wrapper"><img class="lazy-load article-card__image"alt="Lesson 11: Hacking C++ ARM 64 (Part 11 - Hacking Character Primitive Datatype)"data-delayed-url="https://media-exp1.licdn.com/dms/image/C4E12AQFDSzbk5SQRCQ/article-cover_image-shrink_720_1280/0/1608839246858?e=1614816000&amp;v=beta&amp;t=6Mcg5FYO_RPESbj150volfLSdhwDzhEPP5gkMFbw7po"/></div><div class="article-card__content"><h3 class="article-card__title"><a class="article-card__title--link"href="/pulse/lesson-11-hacking-c-arm-64-part-character-primitive-kevin-thomas?trk=read_related_article-card_title"data-tracking-control-name="read_related_article-card_title"data-tracking-will-navigate>Lesson 11: Hacking C++ ARM 64 (Part 11 -…</a></h3><p class="article-card__meta-info"><span class="article-card__meta-info-item">December 24, 2020</span></p> <p class="article-card__meta-info article-card__meta-info--counts"></p></div></div><div class="article-card"><div class="article-card__image--wrapper"><img class="lazy-load article-card__image"alt="Lesson 10: Hacking C++ ARM 64 (Part 10 - Debugging Character Primitive Datatype)"data-delayed-url="https://media-exp1.licdn.com/dms/image/C4E12AQFN_zt3eet-dg/article-cover_image-shrink_720_1280/0/1608824113962?e=1614816000&amp;v=beta&amp;t=U8bIw_jz7i2fRpNQ5-3KkInS8mRN7yTFiQmbtChJvf8"/></div><div class="article-card__content"><h3 class="article-card__title"><a class="article-card__title--link"href="/pulse/lesson-10-hacking-c-arm-64-part-debugging-character-kevin-thomas?trk=read_related_article-card_title"data-tracking-control-name="read_related_article-card_title"data-tracking-will-navigate>Lesson 10: Hacking C++ ARM 64 (Part 10 -…</a></h3><p class="article-card__meta-info"><span class="article-card__meta-info-item">December 24, 2020</span></p> <p class="article-card__meta-info article-card__meta-info--counts"></p></div></div></div></div><script src="https://static-exp1.licdn.com/sc/h/axmmnxay5cp51cfo7bfyr1wln" async defer></script><footer class="li-footer"><ul class="li-footer__list"><li class="li-footer__item"><span class="sr-only">LinkedIn</span><icon class="li-footer__copy-logo" data-delayed-url="https://static-exp1.licdn.com/sc/h/b11vnqql8f4abtysggvq9v836"></icon><span class="li-footer__copy-text">&copy; 2020</span></li><li class="li-footer__item"><a href="https://about.linkedin.com?trk=article_reader_footer_footer-about" data-tracking-control-name="article_reader_footer_footer-about" data-tracking-will-navigate class="li-footer__item-link">About</a></li></li><li class="li-footer__item"><a href="https://www.linkedin.com/accessibility?trk=article_reader_footer_footer-accessibility" data-tracking-control-name="article_reader_footer_footer-accessibility" data-tracking-will-navigate class="li-footer__item-link">Accessibility</a></li><li class="li-footer__item"><a href="https://www.linkedin.com/legal/user-agreement?trk=article_reader_footer_footer-user-agreement" data-tracking-control-name="article_reader_footer_footer-user-agreement" data-tracking-will-navigate class="li-footer__item-link">User Agreement</a></li><li class="li-footer__item"><a href="https://www.linkedin.com/legal/privacy-policy?trk=article_reader_footer_footer-privacy-policy" data-tracking-control-name="article_reader_footer_footer-privacy-policy" data-tracking-will-navigate class="li-footer__item-link">Privacy Policy</a></li><li class="li-footer__item"><a href="https://www.linkedin.com/legal/cookie-policy?trk=article_reader_footer_footer-cookie-policy" data-tracking-control-name="article_reader_footer_footer-cookie-policy" data-tracking-will-navigate class="li-footer__item-link">Cookie Policy</a></li><li class="li-footer__item"><a href="https://www.linkedin.com/legal/copyright-policy?trk=article_reader_footer_footer-copyright-policy" data-tracking-control-name="article_reader_footer_footer-copyright-policy" data-tracking-will-navigate class="li-footer__item-link">Copyright Policy</a></li><li class="li-footer__item"><a href="https://brand.linkedin.com/policies?trk=article_reader_footer_footer-brand-policy" data-tracking-control-name="article_reader_footer_footer-brand-policy" data-tracking-will-navigate class="li-footer__item-link">Brand Policy</a></li><li class="li-footer__item"><a href="https://www.linkedin.com/psettings/guest-controls?trk=article_reader_footer_footer-guest-controls" data-tracking-control-name="article_reader_footer_footer-guest-controls" data-tracking-will-navigate class="li-footer__item-link">Guest Controls</a></li><li class="li-footer__item"><a href="https://www.linkedin.com/help/linkedin/answer/34593?lang=en&amp;trk=article_reader_footer_footer-community-guide" data-tracking-control-name="article_reader_footer_footer-community-guide" data-tracking-will-navigate class="li-footer__item-link">Community Guidelines</a></li><li class="li-footer__item"><div class="collapsible-dropdown language-selector collapsible-dropdown--footer language-selector--footer collapsible-dropdown--up language-selector--up"><ul class="collapsible-dropdown__list language-selector__list hidden" role="menu"><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-ar_AE" class="language-selector__link" data-locale="ar_AE" lang="ar_AE">العربية (Arabic)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-cs_CZ" class="language-selector__link" data-locale="cs_CZ" lang="cs_CZ">Čeština (Czech)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-da_DK" class="language-selector__link" data-locale="da_DK" lang="da_DK">Dansk (Danish)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-de_DE" class="language-selector__link" data-locale="de_DE" lang="de_DE">Deutsch (German)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-en_US" class="language-selector__link language-selector__link--selected" data-locale="en_US" lang="en_US"><strong>English (English)</strong></button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-es_ES" class="language-selector__link" data-locale="es_ES" lang="es_ES">Español (Spanish)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-fr_FR" class="language-selector__link" data-locale="fr_FR" lang="fr_FR">Français (French)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-in_ID" class="language-selector__link" data-locale="in_ID" lang="in_ID">Bahasa Indonesia (Bahasa Indonesia)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-it_IT" class="language-selector__link" data-locale="it_IT" lang="it_IT">Italiano (Italian)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-ja_JP" class="language-selector__link" data-locale="ja_JP" lang="ja_JP">日本語 (Japanese)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-ko_KR" class="language-selector__link" data-locale="ko_KR" lang="ko_KR">한국어 (Korean)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-ms_MY" class="language-selector__link" data-locale="ms_MY" lang="ms_MY">Bahasa Malaysia (Malay)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-nl_NL" class="language-selector__link" data-locale="nl_NL" lang="nl_NL">Nederlands (Dutch)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-no_NO" class="language-selector__link" data-locale="no_NO" lang="no_NO">Norsk (Norwegian)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-pl_PL" class="language-selector__link" data-locale="pl_PL" lang="pl_PL">Polski (Polish)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-pt_BR" class="language-selector__link" data-locale="pt_BR" lang="pt_BR">Português (Portuguese)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-ro_RO" class="language-selector__link" data-locale="ro_RO" lang="ro_RO">Română (Romanian)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-ru_RU" class="language-selector__link" data-locale="ru_RU" lang="ru_RU">Русский (Russian)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-sv_SE" class="language-selector__link" data-locale="sv_SE" lang="sv_SE">Svenska (Swedish)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-th_TH" class="language-selector__link" data-locale="th_TH" lang="th_TH">ภาษาไทย (Thai)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-tl_PH" class="language-selector__link" data-locale="tl_PH" lang="tl_PH">Tagalog (Tagalog)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-tr_TR" class="language-selector__link" data-locale="tr_TR" lang="tr_TR">Türkçe (Turkish)</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-zh_CN" class="language-selector__link" data-locale="zh_CN" lang="zh_CN">简体中文 (Chinese (Simplified))</button></li><li class="language-selector__item" role="menuitem"><button data-tracking-control-name="language-selector-zh_TW" class="language-selector__link" data-locale="zh_TW" lang="zh_TW">正體中文 (Chinese (Traditional))</button></li></ul><button class="language-selector__button"aria-expanded="false"data-tracking-control-name="footer-lang-dropdown_trigger"><span class="language-selector__label-text">Language</span><icon class="language-selector__label-chevron" data-delayed-url="https://static-exp1.licdn.com/sc/h/cyolgscd0imw2ldqppkrb84vo" /></button></div></li></ul></footer><code id="article" style="display: none;"><!--{"author":{"username":"mytechnotalent","twitterHandle":null,"articleCount":216,"profilePicture":"https://media-exp1.licdn.com/dms/image/C4E03AQHj9smy0fl_GA/profile-displayphoto-shrink_100_100/0/1560618806133?e=1614816000&v=beta&t=RpflhN90JitKOWGeZX7eoS53-f3VMPviqzm-KAwpwZg","authorId":216920672,"miniProfile":{"headline":"Senior Software Engineer in Test at BluVector, A Comcast Company","followUrl":null,"numFollowers":792,"articlesUrl":null,"url":"https://www.linkedin.com/in/mytechnotalent","numConnections":29357,"influencer":false,"lastName":"Thomas","firstName":"Kevin","numPosts":null,"backgroundImageUrl":null,"postsUrl":null,"imageUrl":"https://media-exp1.licdn.com/dms/image/C4E03AQHj9smy0fl_GA/profile-displayphoto-shrink_100_100/0/1560618806133?e=1614816000&v=beta&t=RpflhN90JitKOWGeZX7eoS53-f3VMPviqzm-KAwpwZg","numArticles":null}},"series":null,"permalink":"assembly-language-basic-malware-reverse-engineering-kevin-m-thomas","articleImage":{"caption":"","imageUrl":"https://media-exp1.licdn.com/dms/image/C4E12AQFHb7sY3kQ_1w/article-cover_image-shrink_600_2000/0/1520170138889?e=1614816000&v=beta&t=ke8dgzkoUWnCXX4DjrlWyn9pKVvKTs9dIz0EOoWfDFo","imageHeight":400,"imageWidth":698},"linkedInArticleUrn":"urn:li:linkedInArticle:6123429913761443840","description":"For a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.","articleUrl":"/pulse/assembly-language-basic-malware-reverse-engineering-kevin-m-thomas","lastModifiedDate":1581697924000,"locale":"en","caption":"","articleUrn":"urn:li:article:8070593670180647249","publishedDate":1459939784000,"content":"\u003cp\u003eFor a complete table of contents of all the lessons please click below as it will give you a brief of each lesson in addition to the topics it will cover. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial\u003c/p\u003e\u003cp\u003eEssential to the discussion of basic reverse engineering is the concept of modern malware analysis. Malware analysis is the understanding and examination of information necessary to respond to a network intrusion.\u003c/p\u003e\u003cp\u003eThis short tutorial will begin with the basic concepts of malware reverse engineering and graduate to an entry-level basic examination of Assembly Language.\u003c/p\u003e\u003cp\u003eThe keys to the kingdom so to speak are rooted in the break-down of the respective suspected malware binary and how to find it on your network and ultimately to contain it.\u003c/p\u003e\u003cp\u003eUpon full identification of the files required for deeper analysis, it is critical to develop signatures to detect malware infections throughout your network whether it be a home based LAN or complex corporate WAN to which malware analysis is necessary to develop host-based and network signatures.\u003c/p\u003e\u003cp\u003eTo begin with the concept of a host-based signature, we need to understand that these are utilized to find malicious code in a target machine. Host-based signatures are also referred to as indicators which can identify files created or edited by the infected code which can make hidden changes to a computers registry. This is quite in contrast with antivirus signatures because these concentrate on what the malware actually does rather than the make-up of the malware which makes them more effective in finding malware that can migrate or has been removed from the media.\u003c/p\u003e\u003cp\u003eIn contrast, network signatures are used to find malicious code by examining network traffic. It is important to note such tools as WireShark and the like are often effective in such analysis.\u003c/p\u003e\u003cp\u003eUpon identification of these aforementioned signatures, the next step is to identify what the malware is actually doing.\u003c/p\u003e\u003cp\u003e\u003cstrong\u003eUNDER NO CONDITIONS ARE YOU TO EVER USE THIS EDUCATION TO CAUSE HARM TO ANY SYSTEM OF ANY KIND AS I AM NOT RESPONSIBLE! THIS IS FOR LEARNING PURPOSES ONLY!\u003c/strong\u003e\u003c/p\u003e\u003cp\u003eIn our next lesson we will discuss techniques of malware analysis.\u003c/p\u003e","socialActivityCounts":{"numLikes":56,"numComments":0,"numShares":0,"threadHasAction":false},"title":"Assembly Language - Basic Malware Reverse Engineering (Part 1:  Goals)","ugcPost":null,"comments":null}--></code><script data-delayed-url="https://static-exp1.licdn.com/sc/h/9x1ka0d4advijnuxgxnyns6ne" data-module-id="google-one-tap-lib"></script><script src="https://static-exp1.licdn.com/sc/h/ec4mdgijccslffs14mpzdyffn" async></script></body></html>'''

s = BeautifulSoup(htm, 'html.parser')
la = s.find('section', attrs={'class': 'article-body'})
print(la)