gemini.suite('yandex-search', (suite) => {
    suite.setUrl('/')
        .setCaptureElements('.home-logo')
        .capture('plain');
});
