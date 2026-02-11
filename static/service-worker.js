self.addEventListener("install", event => {
  event.waitUntil(
    caches.open("disaster-cache").then(cache => {
      return cache.addAll(["/"]);
    })
  );
});
