const { fetch: originalFetch } = window;

window.fetch = async (...args) => {
    let [resource, config] = args;

    if (config && config.body) {
        const payload = JSON.parse(config.body);
        if (payload.symbol === "RELIANCE" && myLocalCache["RELIANCE"]) {
            console.log("Serving from local cache, no API hit!");
            return new Response(JSON.stringify(myLocalCache["RELIANCE"]));
        }
    }

    return originalFetch(resource, config);
};