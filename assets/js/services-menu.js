(function () {
  const SOURCE_HOST = 'uae.igordar.com';
  const PROJECT_FOLDER = 'uae.igordar.com';
  const LOCAL_PAGES = new Map([
    ['diagnosticheskiy-priem', 'diagnosticheskiy-priem/index.html'],
    ['konsultatsiya-psihologa-online', 'konsultatsiya-psihologa-online/index.html'],
    ['konsultatsiya-psihoterapevta-online', 'konsultatsiya-psihoterapevta-online/index.html'],
    ['konsultatsiya-psihiatra-online', 'konsultatsiya-psihiatra-online/index.html'],
    ['lechenie-bessonnitsy', 'lechenie-bessonnitsy/index.html'],
    ['lechenie-vygoraniya', 'lechenie-vygoraniya/index.html'],
    ['lechenie-depressii', 'lechenie-depressii/index.html'],
    ['lechenie-nevroza', 'lechenie-nevroza/index.html'],
    ['lechenie-panicheskih-atak', 'lechenie-panicheskih-atak/index.html'],
    ['lechenie-ptsr', 'lechenie-ptsr/index.html'],
    ['lechenie-mizantropii', 'lechenie-mizantropii/index.html'],
    ['lechenie-igromanii', 'lechenie-igromanii/index.html'],
    ['lechenie-ipohondrii', 'lechenie-ipohondrii/index.html'],
    ['lechenie-psihopatii', 'lechenie-psihopatii/index.html'],
    ['lechenie-trevozhnosti', 'lechenie-trevozhnosti/index.html'],
    ['lechenie-agorafobii', 'lechenie-agorafobii/index.html'],
    ['lechenie-arahnofobii', 'lechenie-arahnofobii/index.html'],
    ['lechenie-klaustrofobii', 'lechenie-klaustrofobii/index.html'],
    ['lechenie-sotsiofobii', 'lechenie-sotsiofobii/index.html'],
    ['lechenie-filofobii', 'lechenie-filofobii/index.html'],
    ['lechenie-emetofobii', 'lechenie-emetofobii/index.html'],
    ['service', 'service/index.html'],
    ['contacts', 'contacts/index.html'],
    ['liczenziya', 'liczenziya/index.html'],
    ['nashi-filialy', 'nashi-filialy/index.html']
  ]);

  const getProjectRoot = () => {
    if (window.location.origin && window.location.origin !== 'null') {
      return window.location.origin.replace(/\/$/, '') + '/';
    }

    const currentHref = window.location.href;
    const marker = `/${PROJECT_FOLDER}/`;
    const markerIndex = currentHref.indexOf(marker);

    if (markerIndex !== -1) {
      return currentHref.substring(0, markerIndex + marker.length);
    }

    const parts = currentHref.split('/');
    parts.pop();
    return parts.join('/') + '/';
  };

  const getSlug = (href) => {
    if (!href) {
      return null;
    }

    try {
      const url = new URL(href, window.location.href);
      if (url.hostname && !url.hostname.endsWith(SOURCE_HOST)) {
        return null;
      }

      const path = url.pathname.replace(/^\/+/, '');
      const [slug] = path.split('/');
      return slug || null;
    } catch (error) {
      return null;
    }
  };

  const rewriteLinks = () => {
    const projectRoot = getProjectRoot();
    const anchors = document.querySelectorAll('a[href^="https://uae.igordar.com/"]');

    anchors.forEach((anchor) => {
      const slug = getSlug(anchor.getAttribute('href'));
      if (!slug || !LOCAL_PAGES.has(slug)) {
        return;
      }

      const relativePath = LOCAL_PAGES.get(slug);
      anchor.setAttribute('href', projectRoot + relativePath);
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', rewriteLinks);
  } else {
    rewriteLinks();
  }
})();
