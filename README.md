# Phân tích cảm xúc theo khía cạnh cho các đánh giá về sản phẩm sách - truyện

Trong bối cảnh công nghệ phát triển vượt bậc, việc phân tích và hiểu rõ cảm xúc
của khách hàng đã trở thành một yếu tố then chốt giúp các doanh nghiệp nâng
cao chất lượng dịch vụ và tạo dựng lòng tin từ khách hàng. Ngành hàng sách, với
sự đa dạng về sản phẩm và sự cạnh tranh ngày càng gay gắt, cũng không nằm
ngoài xu hướng này. Hiểu được cảm xúc của khách hàng không chỉ giúp các nhà
kinh doanh cải thiện dịch vụ mà còn định hướng chiến lược kinh doanh một cách
hiệu quả hơn.

Dự án ‘Phân tích cảm xúc khách hàng trong ngành
hàng Sách’ nhằm mục đích áp dụng các kỹ thuật xử lý ngôn ngữ tự nhiên và máy
học để thu thập, phân tích và đánh giá cảm xúc của khách hàng qua các đánh giá
và bình luận trên các nền tảng trực tuyến. Qua đó, nghiên cứu không chỉ đưa ra
cái nhìn tổng quan về cảm xúc của khách hàng mà còn đề xuất các biện pháp cải
thiện dựa trên kết quả phân tích.

## Bộ dữ liệu

Chúng tôi đã xây dựng một tập dữ liệu tiếng Việt cho nhiệm vụ phân tích cảm
xúc theo khía cạnh. Tập dữ liệu này chứa các đánh giá bằng tiếng Việt về nhiều
loại sách - truyện như: sách tâm lý, sách self-help, tiểu thuyết nước ngoài, truyện
tranh... được crawl từ sàn thương mại điện tử [Tiki](https://tiki.vn/)

## Phương pháp

1. Dữ liệu được crawl từ sàn thương mại điện tử Tiki, sử dụng Python.
2. Dữ liệu được tiền xử lý, sử dụng Python.
3. Dữ liệu được đánh nhãn, sử dụng [Label Studio](https://labelstud.io/).
4. Sau khi đánh nhãn, dữ liệu được sử dụng để huấn luyện mô hình phân tích cảm xúc theo khía cạnh.
5. Đánh giá mô hình.
