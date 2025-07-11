
from picker.smart_outfit_picker import smartoutfitpicker

def main():
    recommender = smartoutfitpicker('data/outfits.csv')
    print("Recommendations for color='Blue', occasion='Casual':")
    print(recommender.recommend(color='Blue', occasion='Casual'))

    print("\nRecommendations for color='Black', occasion='Formal':")
    print(recommender.recommend(color='Black', occasion='Formal'))

if __name__ == "__main__":
    main()
