// --- 1. TỪ ĐIỂN DỊCH THUẬT (MAPPING ID -> TIẾNG VIỆT) ---
// Đây là danh sách đối chiếu để đảm bảo mọi category đều có tên tiếng Việt đẹp
const categoryTranslations = {
    // Nhóm Sức khỏe & Làm đẹp
    'health_beauty': 'Sức khỏe & Sắc đẹp',
    'perfumery': 'Nước hoa',
    'diapers_and_hygiene': 'Tã & Vệ sinh',
    
    // Nhóm Công nghệ
    'computers_accessories': 'Máy tính & Phụ kiện',
    'telephony': 'Điện thoại & Viễn thông',
    'fixed_telephony': 'Điện thoại cố định',
    'tablets_printing_image': 'Máy tính bảng & In ấn',
    'console_games': 'Máy chơi game', // Sửa lỗi chính tả trong dữ liệu gốc nếu có
    'consoles_games': 'Máy chơi game',
    'audio': 'Thiết bị Âm thanh',
    'electronics': 'Điện tử',
    'computers': 'Máy tính bộ',
    'pc_gamer': 'PC Gaming',
    'cine_photo': 'Máy ảnh & Quay phim',

    // Nhóm Xe cộ
    'auto': 'Ô tô & Xe máy',

    // Nhóm Nhà cửa & Đời sống
    'bed_bath_table': 'Chăn Ga Gối Nệm',
    'furniture_decor': 'Trang trí nội thất',
    'housewares': 'Đồ gia dụng',
    'home_appliances': 'Thiết bị gia đình',
    'home_appliances_2': 'Thiết bị gia đình (Lớn)',
    'small_appliances': 'Thiết bị nhỏ',
    'small_appliances_home_oven_and_coffee': 'Lò nướng & Máy pha cà phê',
    'air_conditioning': 'Điều hòa không khí',
    'home_confort': 'Tiện nghi gia đình',
    'home_comfort_2': 'Tiện nghi gia đình (Khác)',
    'kitchen_dining_laundry_garden_furniture': 'Nội thất Bếp & Vườn',
    'furniture_living_room': 'Nội thất phòng khách',
    'furniture_bedroom': 'Nội thất phòng ngủ',
    'office_furniture': 'Nội thất văn phòng',
    'furniture_mattress_and_upholstery': 'Nệm & Sofa',
    'la_cuisine': 'Dụng cụ nhà bếp',
    'flowers': 'Hoa tươi',
    'garden_tools': 'Làm vườn & Ngoài trời',

    // Nhóm Xây dựng & Công cụ (Đã bổ sung đầy đủ)
    'construction_tools_construction': 'Dụng cụ xây dựng',
    'construction_tools_lights': 'Đèn xây dựng',
    'construction_tools_safety': 'Bảo hộ lao động',
    'costruction_tools_garden': 'Dụng cụ làm vườn', // Giữ nguyên lỗi chính tả từ data gốc
    'costruction_tools_tools': 'Bộ dụng cụ đa năng', // Giữ nguyên lỗi chính tả từ data gốc
    'home_construction': 'Vật liệu xây dựng',

    // Nhóm Thời trang
    'fashion_bags_accessories': 'Túi xách & Thời trang',
    'fashion_shoes': 'Giày dép',
    'fashion_male_clothing': 'Thời trang Nam',
    'fashio_female_clothing': 'Thời trang Nữ', // Giữ nguyên lỗi chính tả từ data gốc
    'fashion_underwear_beach': 'Đồ lót & Đồ bơi',
    'fashion_sport': 'Thời trang thể thao',
    'fashion_childrens_clothes': 'Thời trang trẻ em',
    'watches_gifts': 'Đồng hồ & Quà tặng',
    'luggage_accessories': 'Vali & Du lịch',

    // Nhóm Giải trí & Sở thích
    'sports_leisure': 'Thể thao & Dã ngoại',
    'toys': 'Đồ chơi',
    'baby': 'Mẹ & Bé',
    'cool_stuff': 'Đồ công nghệ Độc lạ',
    'musical_instruments': 'Nhạc cụ',
    'music': 'Âm nhạc',
    'books_general_interest': 'Sách tổng hợp',
    'books_imported': 'Sách ngoại văn',
    'books_technical': 'Sách kỹ thuật',
    'cds_dvds_musicals': 'CD/DVD Nhạc',
    'dvds_blu_ray': 'Đĩa DVD & Blu-ray',
    'art': 'Nghệ thuật',
    'arts_and_craftmanship': 'Thủ công mỹ nghệ',
    'party_supplies': 'Đồ tiệc tùng',
    'christmas_supplies': 'Đồ trang trí Giáng sinh',
    'stationery': 'Văn phòng phẩm',
    'pet_shop': 'Thú cưng',

    // Nhóm Thực phẩm
    'food_drink': 'Thực phẩm & Đồ uống',
    'food': 'Thực phẩm',
    'drinks': 'Đồ uống',

    // Nhóm Khác & Công nghiệp
    'market_place': 'Siêu thị Online',
    'signaling_and_security': 'An ninh & Giám sát',
    'security_and_services': 'An ninh & Dịch vụ',
    'industry_commerce_and_business': 'Công nghiệp & Thương mại',
    'agro_industry_and_commerce': 'Nông nghiệp & Thương mại'
};

// --- 2. DỮ LIỆU SẢN PHẨM CHI TIẾT (CÓ ẢNH & GIÁ CỤ THỂ) ---
// Chỉ cần định nghĩa những món bạn muốn hiển thị đẹp ở trang chủ (Shop Grid)
const featuredProducts = {
    'computers_accessories': { price: 250000, img: 'https://cdn-icons-png.flaticon.com/512/3076/3076404.png' },
    'bed_bath_table': { price: 450000, img: 'https://cdn-icons-png.flaticon.com/512/3028/3028684.png' },
    'furniture_decor': { price: 150000, img: 'https://cdn-icons-png.flaticon.com/512/2558/2558066.png' },
    'sports_leisure': { price: 300000, img: 'https://cdn-icons-png.flaticon.com/512/2964/2964514.png' },
    'health_beauty': { price: 199000, img: 'https://cdn-icons-png.flaticon.com/512/3163/3163212.png' },
    'watches_gifts': { price: 890000, img: 'https://cdn-icons-png.flaticon.com/512/2855/2855589.png' },
    'audio': { price: 550000, img: 'https://cdn-icons-png.flaticon.com/512/3050/3050239.png' },
    'cool_stuff': { price: 350000, img: 'https://cdn-icons-png.flaticon.com/512/2888/2888692.png' },
    'baby': { price: 120000, img: 'https://cdn-icons-png.flaticon.com/512/3063/3063189.png' },
    'auto': { price: 750000, img: 'https://cdn-icons-png.flaticon.com/512/2554/2554936.png' },
    'housewares': { price: 220000, img: 'https://cdn-icons-png.flaticon.com/512/3081/3081840.png' },
    'toys': { price: 90000, img: 'https://cdn-icons-png.flaticon.com/512/3081/3081944.png' },
    'garden_tools': { price: 180000, img: 'https://cdn-icons-png.flaticon.com/512/1518/1518963.png' },
    'office_furniture': { price: 1200000, img: 'https://cdn-icons-png.flaticon.com/512/2663/2663520.png' },
    'telephony': { price: 3500000, img: 'https://cdn-icons-png.flaticon.com/512/900/900461.png' },
    'pet_shop': { price: 85000, img: 'https://cdn-icons-png.flaticon.com/512/3047/3047928.png' },
    'consoles_games': { price: 4500000, img: 'https://cdn-icons-png.flaticon.com/512/3097/3097956.png' }
};

// --- HÀM HELPER: LẤY THÔNG TIN SẢN PHẨM (TỐI ƯU HÓA) ---
function getProductInfo(id) {
    // 1. Tìm tên tiếng Việt
    // Ưu tiên lấy từ từ điển categoryTranslations
    let name = categoryTranslations[id];
    
    // Nếu không có trong từ điển, dùng thuật toán "Làm đẹp tên" (Fallback)
    if (!name) {
        name = id.split('_')
            .map(word => word.charAt(0).toUpperCase() + word.slice(1)) // Viết hoa chữ cái đầu
            .join(' ');
    }

    // 2. Tìm thông tin chi tiết (Giá, Ảnh)
    // Nếu là sản phẩm nổi bật (có trong featuredProducts), lấy giá và ảnh xịn
    let details = featuredProducts[id];
    
    if (!details) {
        // Nếu không có, dùng dữ liệu mặc định
        details = {
            price: 150000, // Giá mặc định
            img: 'https://cdn-icons-png.flaticon.com/512/3081/3081840.png' // Ảnh mặc định (Hộp quà)
        };
    }

    return { 
        id: id,
        name: name, 
        price: details.price, 
        img: details.img 
    };
}

// --- 2. LOGIC DASHBOARD (TAB 1) ---
function initDashboard() {
    const data = window.dashboardData || {};

    // A. Revenue Chart
    if (data.revenueChart) {
        const ctxRev = document.getElementById('revenueChart').getContext('2d');
        new Chart(ctxRev, {
            type: 'line',
            data: {
                labels: data.revenueChart.labels,
                datasets: [{
                    label: 'Doanh Thu (BRL)',
                    data: data.revenueChart.values,
                    borderColor: '#EE4D2D',
                    backgroundColor: 'rgba(238, 77, 45, 0.1)',
                    tension: 0.3,
                    fill: true,
                    pointRadius: 4,
                    pointHoverRadius: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: { beginAtZero: true, grid: { borderDash: [5, 5] } },
                    x: { grid: { display: false } }
                }
            }
        });
    }

    // B. Segmentation Chart
    if (data.segmentChart) {
        const ctxSeg = document.getElementById('segmentChart').getContext('2d');
        new Chart(ctxSeg, {
            type: 'doughnut',
            data: {
                labels: data.segmentChart.labels,
                datasets: [{
                    data: data.segmentChart.values,
                    backgroundColor: ['#3B82F6', '#10B981', '#F59E0B', '#EF4444'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'bottom' }
                }
            }
        });
    }
}

// --- 3. LOGIC SHOPPING (TAB 2) ---
let cart = [];

function initShop() {
    const grid = document.getElementById('product-grid');
    grid.innerHTML = '';
    
    // Render các sản phẩm nổi bật (Featured)
    for (const [key, details] of Object.entries(featuredProducts)) {
        // Sử dụng getProductInfo để lấy tên tiếng Việt chuẩn nhất
        const info = getProductInfo(key);
        
        const html = `
            <div class="product-card bg-white p-4 rounded-lg shadow-sm border border-gray-100 flex flex-col items-center text-center cursor-pointer relative group" onclick="addToCart('${key}')">
                <div class="w-24 h-24 mb-3 flex items-center justify-center bg-gray-50 rounded-full">
                    <img src="${info.img}" class="w-16 h-16 object-contain opacity-90 group-hover:scale-110 transition-transform">
                </div>
                <h3 class="font-bold text-gray-700 text-sm h-10 line-clamp-2">${info.name}</h3>
                <p class="text-red-500 font-bold mt-1">${info.price.toLocaleString()}₫</p>
                <div class="mt-2 text-xs text-gray-400">Đã bán 1.2k</div>
                
                <button class="absolute top-2 right-2 bg-blue-500 text-white w-8 h-8 rounded-full shadow-lg opacity-0 group-hover:opacity-100 transition-all hover:bg-blue-600 flex items-center justify-center">
                    <i class="fa-solid fa-plus"></i>
                </button>
            </div>
        `;
        grid.innerHTML += html;
    }
}

function addToCart(productId) {
    const existing = cart.find(item => item.id === productId);
    if (existing) {
        existing.qty++;
    } else {
        cart.push({ id: productId, qty: 1 });
    }
    updateCartUI();
    updateRecommendations(productId);
}

function removeFromCart(productId) {
    cart = cart.filter(item => item.id !== productId);
    updateCartUI();
    // Nếu giỏ hàng trống, ẩn gợi ý
    if (cart.length === 0) {
        document.getElementById('ai-panel').classList.add('hidden');
    }
}

function updateCartUI() {
    const list = document.getElementById('cart-items');
    const countEl = document.getElementById('cart-count');
    const totalEl = document.getElementById('cart-total');
    
    // Update count
    const totalQty = cart.reduce((sum, item) => sum + item.qty, 0);
    countEl.innerText = totalQty;
    
    // Render list
    if (cart.length === 0) {
        list.innerHTML = `
            <div class="text-center py-6 text-gray-400 text-sm">
                <i class="fa-solid fa-basket-shopping text-3xl mb-2 opacity-50"></i><br>
                Giỏ hàng trống
            </div>`;
        totalEl.innerText = '0₫';
        return;
    }

    list.innerHTML = '';
    let grandTotal = 0;
    
    cart.forEach(item => {
        // Dùng hàm getProductInfo thay vì truy xuất trực tiếp
        const info = getProductInfo(item.id);
        const total = info.price * item.qty;
        grandTotal += total;
        
        list.innerHTML += `
            <div class="cart-item flex items-center gap-3 bg-gray-50 p-2 rounded border border-gray-100 mb-2">
                <img src="${info.img}" class="w-10 h-10 object-contain">
                <div class="flex-1 min-w-0">
                    <div class="text-xs font-bold text-gray-700 truncate">${info.name}</div>
                    <div class="text-xs text-gray-500">${info.price.toLocaleString()}₫ x ${item.qty}</div>
                </div>
                <button onclick="removeFromCart('${item.id}')" class="text-gray-400 hover:text-red-500 p-1">
                    <i class="fa-solid fa-trash text-xs"></i>
                </button>
            </div>
        `;
    });

    totalEl.innerText = grandTotal.toLocaleString() + '₫';
}

function updateRecommendations(lastItemId) {
    const rules = window.dashboardData?.rules || {};
    const suggestions = rules[lastItemId];
    const panel = document.getElementById('ai-panel');
    const list = document.getElementById('recommendation-list');

    if (!suggestions || suggestions.length === 0) {
        return; 
    }

    // Lọc những món chưa có trong giỏ
    const validSuggestions = suggestions.filter(suggId => !cart.find(c => c.id === suggId));

    if (validSuggestions.length > 0) {
        list.innerHTML = '';
        // Lấy tối đa 3 gợi ý
        validSuggestions.slice(0, 3).forEach(suggId => {
            // Dùng hàm getProductInfo để lấy tên đẹp hoặc fallback
            const info = getProductInfo(suggId);
            
            list.innerHTML += `
                <div class="recommendation-item flex items-center gap-2 bg-white p-2 rounded border border-indigo-100 hover:border-indigo-300 cursor-pointer transition" onclick="addToCart('${suggId}')">
                    <img src="${info.img}" class="w-8 h-8 object-contain">
                    <div class="flex-1 min-w-0">
                        <div class="text-xs font-bold text-indigo-900 truncate">${info.name}</div>
                        <div class="text-[10px] text-gray-500">Thường mua cùng</div>
                    </div>
                    <div class="w-5 h-5 bg-indigo-100 text-indigo-600 rounded-full flex items-center justify-center hover:bg-indigo-600 hover:text-white transition">
                        <i class="fa-solid fa-plus text-[10px]"></i>
                    </div>
                </div>
            `;
        });
        panel.classList.remove('hidden');
    }
}

// --- 4. TAB SWITCHING ---
function switchTab(tabId) {
    // Hide all
    document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
    document.querySelectorAll('.nav-btn').forEach(el => {
        el.classList.remove('active', 'text-yellow-400', 'border-yellow-400');
        el.classList.add('text-gray-400');
    });

    // Show active
    document.getElementById(`tab-${tabId}`).classList.remove('hidden');
    const btn = document.getElementById(`btn-${tabId}`);
    btn.classList.add('active', 'text-yellow-400');
    btn.classList.remove('text-gray-400');
}

function checkout() {
    if (cart.length === 0) return alert("Giỏ hàng trống!");
    alert("Cảm ơn bạn đã mua hàng! (Demo kết thúc)");
    cart = [];
    updateCartUI();
    document.getElementById('ai-panel').classList.add('hidden');
}

// --- INIT ---
window.onload = function() {
    initDashboard();
    initShop();
    switchTab('dashboard');
};