
class Sources:
    # ------------------------------------------------> TWITTER <-------------------------------------------------------- #
    # 1. Twitter Users to Monitor
    twitter_users = ['mcuban', 'elonmusk', 'PeterLBrandt', 'CNBC', 'SJosephBurns', 'elerianm', 'IBDinvestors', 'jimcramer',
                     'bespokeinvest', 'wsbmod', 'galgitron', 'thevrsoldier', 'glewmecorp']
    twitter_users_test = ['mcuban', 'elonmusk']
    # ------------------------------------------------> REDDIT <--------------------------------------------------------- #
    # 1. Crypto Subreddit Communities to Monitor
    reddit_communities_test = ['altstreetbets']
    reddit_communities = ['altstreetbets', 'CryptoCurrency', 'CryptoCurrencies', 'CryptoMarkets', 'cryptosignals',
                          'cryptospread', 'satoshistreetbets', 'wallstreetbets', 'WallStreetbetsELITE',
                          'deepfuckingvalue', 'stocks', 'investing', 'stockmarket']

    # 2. Stock Subreddit Communities to Monitor
    stocks_reddit_communities = ['wallstreetbets', 'WallStreetbetsELITE', 'deepfuckingvalue', 'stocks', 'investing',
                                 'stockmarket']

    # 3. Posts flairs to search || None flair is automatically considered
    post_flair = {'Daily Discussion', 'Weekend Discussion', 'Ticker Discussion', 'Discussion',
                  'General News', 'Fundamentals', 'News', 'Gain', 'OFFICIAL', 'META', 'TRADING',
                  'EDUCATIONAL', 'FOCUSED-DISCUSSION', 'Technical Analysis'}

    # 4. Granted Users to Monitor
    users_to_grant = {'DeepFuckingValue'}

    metaverse_crypto_symbols = ["ETH", "MANA", "SAND", "AXS", "THETA", "ENJ", "WAX", "SUSHI", "CEEK"]

    master_rss_list = [
        "http://bankautomationnews.com/feed/",
        "http://feeds.arstechnica.com/arstechnica/technology-lab",
        "http://feeds.bbci.co.uk/news/technology/rss.xml",
        "http://feeds.betanews.com/bn",
        "http://feeds.feedblitz.com/freetech4teachers",
        "http://feeds.feedburner.com/IeeeSpectrumFullText",
        "http://feeds.feedburner.com/TalkTechToMe-All",
        "http://feeds.feedburner.com/Techeblog",
        "http://feeds.feedburner.com/oreilly/radar/atom",
        "http://feeds.feedburner.com/techdirt/feed",
        "http://feeds.feedburner.com/techgyd",
        "http://feeds.feedburner.com/venturebeat/SZYF",
        "http://feeds.findlaw.com/FLTechnologist",
        "http://feeds.haowtogeek.com/HowToGeek",
        "http://feeds.washingtonpost.com/rss/business/technology",
        "http://fintechprofile.com/feed",
        "http://fintechranking.com/category/news/feed/",
        "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
        "http://tech.firstpost.com/feed",
        "http://techenger.com/feed",
        "http://uploadvr.com/feed",
        "http://voguepayblog.com/blog/feed/",
        "http://vrscout.com/feed",
        "http://www.campaignlive.co.uk/rss/brand/tech",
        "http://www.computerworld.com/index.rss",
        "http://www.extremetech.com/feed",
        "http://www.fintech.finance/feed/",
        "http://www.fintechrising.co/feed/",
        "http://www.fintechsv.com/feed",
        "http://www.infoworld.com/index.rss",
        "http://www.itworldcanada.com/feed",
        "http://www.macworld.com/index.rss",
        "http://www.roadtovr.com/feed",
        "http://www.techhive.com/index.rss",
        "http://www.technobuffalo.com/feed/",
        "http://www.techspot.com/backend.xml",
        "http://www.theregister.co.uk/headlines.atom",
        "http://www.theverge.com/rss/frontpage",
        "http://www.vrfocus.com/feed",
        "https://alicekeeler.com/feed/",
        "https://appleinsider.com/rss/news/",
        "https://australianfintech.com.au/blog/feed/",
        "https://ayorkshiregirltravels.com/feed/",
        "https://bankingtransformed.libsyn.com/rss",
        "https://bankloch.blogspot.com/feeds/posts/default",
        "https://bgr.com/tech/feed/",
        "https://bilderlings.com/blog/feed/",
        "https://blog.dgwbirch.com/?feed=rss2",
        "https://blog.imarticus.org/feed/",
        "https://blog.xtrm.com/category/feed/Blog",
        "https://blogs.nvidia.com/blog/category/virtual-reality/feed",
        "https://castlightfinancial.com/feed/",
        "https://chyp.com/thought-leaders/blog/feed/",
        "https://cosaic.io/category/fintech/feed/",
        "https://dailyfintech.com/feed/",
        "https://defirepublic.com/feed/",
        "https://dongknows.com/feed/",
        "https://earnix.com/blog/feed/",
        "https://engineerbabu.com/blog/feed/",
        "https://eufintech.blogspot.com/feeds/posts/default",
        "https://feeds.feedburner.com/RedmondPie",
        "https://finovate.com/feed/",
        "https://fintecbuzz.com/feed/",
        "https://fintechnews.ch/feed/",
        "https://fintechnews.hk/feed/",
        "https://fintechnews.sg/feed/",
        "https://fintechreview.net/feed",
        "https://finteknews.com/feed",
        "https://finvsfin.com/feed/",
        "https://forkast.news/feed/",
        "https://gigaom.com/feed/",
        "https://gizmodo.com/tag/virtual-reality/rss",
        "https://globalfintechnews.com/feed/",
        "https://globallending.fortunellc.us/feeds/posts/default?alt=rss",
        "https://group.growvc.com/news/feed",
        "https://habiletechnologies.com/feed/",
        "https://hackaday.com/blog/feed/",
        "https://hackernoon.com/feed",
        "https://hardbacon.ca/en/feed/",
        "https://hollandfintech.com/feed/",
        "https://investingintheweb.com/feed/",
        "https://irishtechnews.ie/feed/",
        "https://itchronicles.com/feed/",
        "https://jessicaellerm.com/feed/?x=1",
        "https://kae.com/ideabank/blog-archive/feed",
        "https://lendfoundry.com/feed/",
        "https://meawallet.com/blog/feed/",
        "https://medium.com/feed/@Within",
        "https://medium.com/feed/edtech-trends",
        "https://medium.com/feed/wharton-fintech",
        "https://merchantalternatives.com/feed",
        "https://mobilesyrup.com/feed/",
        "https://ncfacanada.org/feed/",
        "https://news.google.com/rss/search?q=virtual+reality+news&hl=en-US&gl=US&ceid=US%3Aen",
        "https://nextmoney.org/feed",
        "https://psplab.com/fintech-blog/feed/",
        "https://readdive.com/feed/",
        "https://readwrite.com/feed/?x=1",
        "https://risksave.com/news?format=RSS",
        "https://rss2.feedspot.com/https://gomedici.com/",
        "https://rss2.feedspot.com/https://zootsolutions.com/blog/?context=3338134623",
        "https://sifted.eu/feed/?post_type=article",
        "https://siliconangle.com/feed/",
        "https://tap2pay.me/blog/feed/",
        "https://techaeris.com/feed/",
        "https://techbullion.com/feed/",
        "https://techengage.com/feed",
        "https://techresearchonline.com/feed/",
        "https://thefinancialbrand.com/fintech/feed/",
        "https://thefinanser.com/category/fintech/feed/",
        "https://thefintechtimes.com/feed/",
        "https://thenextweb.com/topic/tech",
        "https://thisisoliver.co/feed/",
        "https://veer.tv/blog/feed",
        "https://virtualrealityreporter.com/feed",
        "https://vulcanpost.com/feed/",
        "https://www.afritechmedia.com/feed/",
        "https://www.alepietrocola.com/en/feed/",
        "https://www.amount.com/blog/rss.xml",
        "https://www.anandtech.com/rss/",
        "https://www.area19delegate.org/feed/",
        "https://www.aretosystems.com/feed/",
        "https://www.atmmarketplace.com/rss/",
        "https://www.bleepingcomputer.com/feed",
        "https://www.blogthetech.com/feed/",
        "https://www.bobsguide.com/feed/",
        "https://www.clarusft.com/feed/",
        "https://www.cnet.com/rss/news/",
        "https://www.datadriveninvestor.com/feed/",
        "https://www.dcrstrategies.com/feed/",
        "https://www.digfingroup.com/feed/",
        "https://www.digitaltrends.com/virtual-reality/feed",
        "https://www.droid-life.com/feed/",
        "https://www.droidviews.com/feed/",
        "https://www.ecoustics.com/feed",
        "https://www.edsurge.com/articles_rss",
        "https://www.etoro.com/blog/feed/",
        "https://www.financemagnates.com/fintech/feed/",
        "https://www.finextra.com/rss/blogs.aspx/?x=1",
        "https://www.fintechaustralia.org.au/feed/",
        "https://www.fintechfutures.com/feed/",
        "https://www.fintechinshorts.com/feed/",
        "https://www.fintechlawblog.com/feed/",
        "https://www.fintechmarketinghub.com/blog-feed.xml",
        "https://www.fintechtris.com/blog?format=rss",
        "https://www.fintechupdate.com/feed/",
        "https://www.fintechweekly.com/feed",
        "https://www.forbes.com/sites/tomgroenfeldt/feed/",
        "https://www.geekwire.com/feed/",
        "https://www.holtaccelerator.ai/feed/",
        "https://www.hydrogenplatform.com/blog/feed",
        "https://www.hypergridbusiness.com/feed/",
        "https://www.ilounge.com/feed",
        "https://www.intelalley.com/feed/",
        "https://www.ishir.com/feed/",
        "https://www.kantox.com/en/feed/",
        "https://www.kunal-chowdhury.com/feeds/posts/default",
        "https://www.lemnisk.co/blog/feed/",
        "https://www.lendingkart.com/feed/",
        "https://www.linklaters.com/en/rss-feeds/fintechlinks",
        "https://www.mobilepaymentstoday.com/rss/",
        "https://www.onpaysolutions.com/payment-blog/rss.xml",
        "https://www.osborneclarke-fintech.com/feed/",
        "https://www.paymentscardsandmobile.com/category/fintech/feed/",
        "https://www.paymentssource.com/feed?rss=true",
        "https://www.pymnts.com/feed/",
        "https://www.reddit.com/r/virtualreality/.rss",
        "https://www.regtechtimes.com/feed/",
        "https://www.rootbranded.com//blog-feed.xml",
        "https://www.rpaywallet.com/blog/feed/",
        "https://www.siliconrepublic.com/feed",
        "https://www.techmeme.com/feed.xml?x=1",
        "https://www.technologyreview.com/topnews.rss",
        "https://www.vox.com/rss/recode/index.xml",
        "https://www.waftr.com/feed/",
        "https://www.wired.com/feed/rss",
        "https://xcelpros.com/feed/",
        "techcrunch.com/feed", "http://www.marketwatch.com/rss/realtimeheadlines",
        "http://www.marketwatch.com/rss/marketpulse", "http://feeds.marketwatch.com/marketwatch/bulletins",
        "http://www.marketwatch.com/rss/topstories", "http://www.marketwatch.com/rss/pf",
        "http://www.marketwatch.com/rss/StockstoWatch", "http://www.marketwatch.com/rss/internet",
        "http://www.marketwatch.com/rss/mutualfunds", "http://www.marketwatch.com/rss/software",
        "http://www.marketwatch.com/rss/financial", "http://www.marketwatch.com/rss/financial",
        "http://www.marketwatch.com/rss/commentary", "http://www.marketwatch.com/rss/newslettersandresearch"
    ]
    master_source_list_test = ["https://www.nytimes.com/",
                               "https://www.foxnews.com/"]
    master_source_list = [
        "https://abcnews.go.com/",
        "https://www.cnn.com/",
        "https://www.nbcnews.com/",
        "https://www.huffingtonpost.com/",
        "https://www.cbsnews.com/",
        "https://www.usatoday.com/",
        "https://www.buzzfeed.com/",
        "https://www.nytimes.com/",
        "https://www.foxnews.com/",
        "https://www.dailymail.co.uk/ushome/index.html",
        "https://www.washingtonpost.com/",
        "https://bleacherreport.com/",
        "https://www.businessinsider.com/",
        "https://elitedaily.com/",
        "https://www.bbc.com/",
        "https://www.cnet.com/",
        "https://www.theguardian.com/us",
        "https://www.msn.com/en-us/news",
        "https://www.npr.org/",
        "https://www.nydailynews.com/",
        "https://www.latimes.com/",
        "https://nypost.com/",
        "https://time.com/",
        "https://mashable.com/",
        "https://www.sfgate.com/",
        "https://www.slate.com/",
        "https://www.upworthy.com/",
        "https://www.theblaze.com/",
        "https://www.telegraph.co.uk/",
        "https://www.usnews.com/",
        "https://www.vice.com/en_us",
        "https://www.chron.com/",
        "https://gawker.com/",
        "https://www.examiner.com/",
        "https://www.vox.com/",
        "https://www.chicagotribune.com/",
        "https://www.thedailybeast.com/",
        "https://www.salon.com/",
        "https://mic.com/",
        "https://www.mirror.co.uk/news/",
        "https://www.nj.com",
        "https://www.independent.co.uk/",
        "https://www.freep.com/",
        "https://www.bostonglobe.com/",
        "https://www.theatlantic.com/",
        "https://www.mlive.com/",
        "https://www.engadget.com/",
        "https://techcrunch.com/",
        "https://www.boston.com",
        "https://www.al.com/",
        "https://www.dallasnews.com/"
    ]


    def sort_rss_list(self):
        sorted_rss_list = sorted(self.master_rss_list)
        return sorted_rss_list

# if __name__ == '__main__':
    # sort_rss_list()
    # print(len(master_rss_list))
